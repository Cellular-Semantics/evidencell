"""MapMyCells GraphQL API client.

Submits mapping jobs to the BKP GraphQL endpoint, uploads files via
signed CloudFront URLs, polls for completion, and downloads results.

Discovered via network capture of knowledge.brain-map.org/mapmycells/process.
No browser automation required — pure HTTP/GraphQL.
"""

from __future__ import annotations

import io
import time
import zipfile
from pathlib import Path
from typing import Any
from uuid import uuid4

import httpx

from annotation_transfer.taxonomies import TaxonomySpec


GRAPHQL_URL = "https://bkp-server-prod.aibs-bmp-prod.net/graphql"
DEFAULT_TIMEOUT = 3600  # 1 hour
POLL_INTERVAL_INITIAL = 5.0
POLL_INTERVAL_MAX = 30.0
POLL_BACKOFF_FACTOR = 1.5


class MapMyCellsAPIError(Exception):
    """Raised when a MapMyCells API call fails."""


class MapMyCellsTimeoutError(MapMyCellsAPIError):
    """Raised when polling exceeds the timeout."""


def _graphql(
    client: httpx.Client,
    operation: str,
    query: str,
    variables: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Execute a GraphQL query and return the data dict."""
    payload: dict[str, Any] = {
        "operationName": operation,
        "query": query,
    }
    if variables is not None:
        payload["variables"] = variables

    resp = client.post(
        GRAPHQL_URL,
        json=payload,
        headers={
            "content-type": "application/json",
            "accept": "*/*",
        },
    )
    resp.raise_for_status()
    body = resp.json()
    if "errors" in body:
        raise MapMyCellsAPIError(
            f"GraphQL error in {operation}: {body['errors']}"
        )
    return body.get("data", {})


def get_workflows(client: httpx.Client) -> list[dict[str, Any]]:
    """List available taxonomies and mapping algorithms."""
    data = _graphql(
        client,
        "getWorkflowNames",
        """query getWorkflowNames {
            getWorkflowNames {
                workflowName
                workflowDisplayName
                reference
                referenceDataDisplayName
                isAlgorithmDefaultForRefData
            }
        }""",
    )
    return data.get("getWorkflowNames", [])


def get_anonymous_uuid(client: httpx.Client) -> str:
    """Get an anonymous session UUID from the server."""
    data = _graphql(
        client,
        "getAnonymousUuid",
        "query getAnonymousUuid { getAnonymousUuid }",
    )
    uuid = data.get("getAnonymousUuid")
    if not uuid:
        # Fall back to client-generated UUID
        return str(uuid4())
    return uuid


def initialize_upload(
    client: httpx.Client,
    file_name: str,
    file_size: int,
    uuid: str,
) -> tuple[str, str]:
    """Initialize an anonymous upload. Returns (signed_url, execution_id)."""
    data = _graphql(
        client,
        "initializeAnonymous",
        """query initializeAnonymous(
            $fileName: String!, $fileSize: String!, $uuid: String!
        ) {
            initializeUploadAnonymous(
                fileName: $fileName, fileSize: $fileSize, uuid: $uuid
            ) {
                signedUrl
                executionID
            }
        }""",
        variables={
            "fileName": file_name,
            "fileSize": str(file_size),
            "uuid": uuid,
        },
    )
    result = data.get("initializeUploadAnonymous", {})
    signed_url = result.get("signedUrl")
    execution_id = result.get("executionID")
    if not signed_url or not execution_id:
        raise MapMyCellsAPIError(
            f"Failed to initialize upload: {result}"
        )
    return signed_url, execution_id


def upload_file(client: httpx.Client, signed_url: str, file_path: Path) -> None:
    """Upload a file to the signed CloudFront URL via PUT."""
    file_bytes = file_path.read_bytes()
    resp = client.put(
        signed_url,
        content=file_bytes,
        headers={
            "x-amz-acl": "bucket-owner-full-control",
            "content-type": "application/x-www-form-urlencoded",
        },
        timeout=600.0,  # 10 min for large files
    )
    resp.raise_for_status()


def trigger_workflow(
    client: httpx.Client,
    execution_id: str,
    workflow_names: list[str],
    reference_taxonomies: list[str],
    uuid: str,
    email: str = "",
) -> dict[str, Any]:
    """Trigger the mapping workflow."""
    data = _graphql(
        client,
        "triggerBkpWorkflowAnonymous",
        """query triggerBkpWorkflowAnonymous(
            $referenceTaxonomies: [String]!,
            $executionID: String!,
            $workflowNames: [String]!,
            $uuid: String!,
            $email: String
        ) {
            triggerBkpWorkflowAnonymous(
                referenceTaxonomies: $referenceTaxonomies,
                executionID: $executionID,
                workflowNames: $workflowNames,
                uuid: $uuid,
                email: $email
            ) {
                result
                JobStatus
            }
        }""",
        variables={
            "referenceTaxonomies": reference_taxonomies,
            "executionID": execution_id,
            "workflowNames": workflow_names,
            "uuid": uuid,
            "email": email,
        },
    )
    return data.get("triggerBkpWorkflowAnonymous", {})


def poll_status(
    client: httpx.Client,
    execution_id: str,
    uuid: str,
    *,
    timeout: float = DEFAULT_TIMEOUT,
    on_status: Any | None = None,
) -> dict[str, Any]:
    """Poll workflow status until completion or failure.

    Parameters
    ----------
    on_status
        Optional callback(status_dict) called on each poll iteration.

    Returns
    -------
    Final status dict with workflowStatus, algorithmStatus, ETA.

    Raises
    ------
    MapMyCellsTimeoutError if timeout exceeded.
    MapMyCellsAPIError if workflow reports failure.
    """
    query = """query getWorkflowStatusAnonymous(
        $executionID: String!, $uuid: String!
    ) {
        getWorkflowStatusAnonymous(
            executionID: $executionID, uuid: $uuid
        ) {
            workflowStatus
            algorithmStatus
            ETA
        }
    }"""

    start = time.monotonic()
    interval = POLL_INTERVAL_INITIAL

    while True:
        elapsed = time.monotonic() - start
        if elapsed > timeout:
            raise MapMyCellsTimeoutError(
                f"Mapping timed out after {timeout}s. "
                f"execution_id={execution_id}"
            )

        data = _graphql(
            client,
            "getWorkflowStatusAnonymous",
            query,
            variables={"executionID": execution_id, "uuid": uuid},
        )
        status = data.get("getWorkflowStatusAnonymous", {})

        if on_status is not None:
            on_status(status)

        workflow_status = status.get("workflowStatus", "")
        algorithm_status = status.get("algorithmStatus", "")

        # Terminal states
        if "FAILED" in workflow_status.upper() or "FAILED" in algorithm_status.upper():
            raise MapMyCellsAPIError(
                f"Mapping failed: workflowStatus={workflow_status}, "
                f"algorithmStatus={algorithm_status}"
            )

        if "SUCCEEDED" in workflow_status.upper() or "COMPLETED" in workflow_status.upper():
            return status

        time.sleep(min(interval, POLL_INTERVAL_MAX))
        interval *= POLL_BACKOFF_FACTOR


def download_result(
    client: httpx.Client,
    execution_id: str,
    uuid: str,
    output_dir: Path,
) -> Path:
    """Download and extract the result ZIP.

    Returns the path to the extracted CSV file.

    Note: The download endpoint discovery is based on the pattern
    observed in the web UI. The exact GraphQL query may need
    refinement once tested with a successful mapping.
    """
    # Try the getDownloadUrl pattern (common in BKP GraphQL)
    data = _graphql(
        client,
        "getDownloadUrlAnonymous",
        """query getDownloadUrlAnonymous(
            $executionID: String!, $uuid: String!
        ) {
            getDownloadUrlAnonymous(
                executionID: $executionID, uuid: $uuid
            ) {
                signedUrl
            }
        }""",
        variables={"executionID": execution_id, "uuid": uuid},
    )
    result = data.get("getDownloadUrlAnonymous", {})
    download_url = result.get("signedUrl")

    if not download_url:
        raise MapMyCellsAPIError(
            f"No download URL returned for execution {execution_id}"
        )

    resp = client.get(download_url, timeout=300.0)
    resp.raise_for_status()

    output_dir.mkdir(parents=True, exist_ok=True)

    # Extract ZIP contents
    zip_path = output_dir / f"{execution_id}.zip"
    zip_path.write_bytes(resp.content)

    csv_path = None
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        for name in zf.namelist():
            zf.extract(name, output_dir)
            if name.endswith(".csv") and "validation_log" not in name:
                csv_path = output_dir / name

    if csv_path is None:
        raise MapMyCellsAPIError(
            f"No CSV found in result ZIP for execution {execution_id}. "
            f"Contents: {zipfile.ZipFile(io.BytesIO(resp.content)).namelist()}"
        )

    return csv_path


def run_mapmycells_web(
    input_path: Path,
    taxonomy: TaxonomySpec,
    algorithm: str,
    output_dir: Path,
    *,
    timeout_seconds: float = DEFAULT_TIMEOUT,
    on_status: Any | None = None,
) -> Path:
    """Submit a file to MapMyCells via the GraphQL API.

    Parameters
    ----------
    input_path
        Path to h5ad or CSV file to map.
    taxonomy
        Taxonomy spec (must have web_ref_id set).
    algorithm
        Workflow name, e.g. "HierarchicalAlgorithmRun".
    output_dir
        Directory for extracted results.
    timeout_seconds
        Max seconds to wait for completion.
    on_status
        Optional callback for status updates during polling.

    Returns
    -------
    Path to the result CSV file.
    """
    if not taxonomy.web_ref_id:
        raise MapMyCellsAPIError(
            f"Taxonomy '{taxonomy.id}' has no web_ref_id — "
            f"cannot submit to MapMyCells web API."
        )

    file_size = input_path.stat().st_size
    file_name = input_path.name

    with httpx.Client(timeout=60.0) as client:
        # 1. Get anonymous UUID
        uuid = get_anonymous_uuid(client)

        # 2. Initialize upload → get signed URL + execution ID
        signed_url, execution_id = initialize_upload(
            client, file_name, file_size, uuid
        )

        # 3. Upload file
        upload_file(client, signed_url, input_path)

        # 4. Trigger workflow
        trigger_workflow(
            client,
            execution_id,
            workflow_names=[algorithm],
            reference_taxonomies=[taxonomy.web_ref_id],
            uuid=uuid,
        )

        # 5. Poll for completion
        poll_status(
            client, execution_id, uuid,
            timeout=timeout_seconds,
            on_status=on_status,
        )

        # 6. Download results
        csv_path = download_result(client, execution_id, uuid, output_dir)

    return csv_path
