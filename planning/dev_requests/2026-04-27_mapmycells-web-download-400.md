# Dev Request: MapMyCells web API download step fails with 400

**Date:** 2026-04-27  
**Blocked step:** `annotation-transfer` → `just at-map` web path  
**Priority:** LOW (local fallback works)

## What is blocked

The `at-map` command (web path) successfully submits jobs to the MapMyCells API and runs them (WORKFLOW_SUCCEEDED), but fails at the result download step with HTTP 400 from the GraphQL endpoint.

Repro:
```
just at-map inputs/datasets/GSE185862_yao2021/hpf_ssv4_mmc.h5ad CCN20230722 outputs/
```

Output:
```
Status: workflow=WORKFLOW_SUCCEEDED algorithm=Mapping algorithm finished successfully.
httpx.HTTPStatusError: Client error '400 Bad Request' for url 'https://bkp-server-prod.aibs-bmp-prod.net/graphql'
```

## Where it fails

`annotation_transfer/src/annotation_transfer/mapper_web.py`, function `download_result()` (line ~269):

```python
def download_result(client, execution_id, uuid, output_dir):
    # Note in code: "The exact GraphQL query may need refinement once tested with a successful mapping"
    data = _graphql(client, "getDownloadUrlAnonymous", """query getDownloadUrlAnonymous(
        $executionID: String!, $uuid: String!
    ) {
        getDownloadUrlAnonymous(executionID: $executionID, uuid: $uuid) {
            signedUrl
        }
    }""", variables={"executionID": execution_id, "uuid": uuid})
```

The query `getDownloadUrlAnonymous` returns 400, suggesting either:
1. The operation name does not exist in the BKP GraphQL schema
2. The `$executionID`/`$uuid` variable format changed
3. Authentication/session state is invalid at download time

## Workaround in use

`just at-map-local` with the precomputed stats at `annotation_transfer/conf/mapmycells/CCN20230722/precomputed_stats.h5` works correctly (exit 0).

## Proposed fix

1. Inspect the BKP GraphQL schema for the correct download query operation name (could be `downloadResult`, `getResultDownloadUrl`, or similar)
2. Test with a real execution_id+uuid pair to confirm the correct query
3. Optionally add a retry/fallback to re-fetch the download URL independently

## What was tried

- Multiple retries: all fail at the same `download_result` step after successful WORKFLOW_SUCCEEDED
- Local fallback (`at-map-local`): works — no code change needed for current curation work
- The fix would unblock the web path for datasets where local stats are unavailable
