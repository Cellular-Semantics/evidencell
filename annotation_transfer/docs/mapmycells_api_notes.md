# MapMyCells GraphQL API — Discovery Notes

> Discovered 2026-04-09 via Playwright network capture of
> `https://knowledge.brain-map.org/mapmycells/process`

## Endpoint

```
POST https://bkp-server-prod.aibs-bmp-prod.net/graphql
Content-Type: application/json
```

All operations use standard GraphQL POST with `operationName`, `query`, and `variables`.

## Complete API Flow

### 1. List available workflows

```graphql
query getWorkflowNames {
  getWorkflowNames {
    workflowName
    workflowDisplayName
    reference
    referenceDataDisplayName
    isAlgorithmDefaultForRefData
  }
}
```

Returns all available taxonomy + algorithm combinations.

### 2. Get anonymous UUID

```graphql
query getAnonymousUuid {
  getAnonymousUuid
}
```

Returns a UUID string for anonymous session tracking.

### 3. Initialize upload

```graphql
query initializeAnonymous($fileName: String!, $fileSize: String!, $uuid: String!) {
  initializeUploadAnonymous(fileName: $fileName, fileSize: $fileSize, uuid: $uuid) {
    signedUrl
    executionID
  }
}
```

- `fileSize` is a **string** (not int)
- Returns a **signed CloudFront URL** for direct file upload
- Returns an `executionID` used for all subsequent operations

### 4. Upload file

```http
PUT <signedUrl>
x-amz-acl: bucket-owner-full-control
Content-Type: application/x-www-form-urlencoded
```

Upload the raw file bytes to the CloudFront CDN URL.
The URL is at `d2bvn9p3huo3el.cloudfront.net/CDM/input/anony-<uuid>/<executionID>/<filename>`.

### 5. Trigger workflow

```graphql
query triggerBkpWorkflowAnonymous(
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
}
```

- `referenceTaxonomies`: e.g. `["10xGene"]`
- `workflowNames`: e.g. `["HierarchicalAlgorithmRun"]`
- `email`: empty string for anonymous

### 6. Poll status

```graphql
query getWorkflowStatusAnonymous($executionID: String!, $uuid: String!) {
  getWorkflowStatusAnonymous(executionID: $executionID, uuid: $uuid) {
    workflowStatus
    algorithmStatus
    ETA
  }
}
```

Poll repeatedly until `workflowStatus` contains "SUCCEEDED" or "FAILED".

### 7. Download results (TBD)

Likely:
```graphql
query getDownloadUrlAnonymous($executionID: String!, $uuid: String!) {
  getDownloadUrlAnonymous(executionID: $executionID, uuid: $uuid) {
    signedUrl
  }
}
```

Returns a signed URL to download a ZIP containing CSV, JSON, and log files.

## Known Taxonomy IDs

| Display Name | `reference` (refTaxonomyId) | URL param |
|---|---|---|
| 10x Whole Mouse Brain (CCN20230722) | `10xGene` | `?refTaxonomyId=10xGene` |
| 10x Whole Human Brain (CCN202210140) | `10x_whole_human_brain` | `?refTaxonomyId=10x_whole_human_brain` |
| 10x Human MTG SEA-AD (CCN20230505) | `10x-Human-MTG-SEA-AD` | `?refTaxonomyId=10x-Human-MTG-SEA-AD` |
| Consensus Basal Ganglia (CCN20250428) | `HMBA-BG-taxonomy-CCN20250428` | `?refTaxonomyId=HMBA-BG-taxonomy-CCN20250428` |

## Known Algorithm Workflow Names

| Taxonomy | Algorithms |
|---|---|
| WMB (10xGene) | `HierarchicalAlgorithmRun`, `CorrelationAlgorithmRun` |
| WHB (10x_whole_human_brain) | `CorrelationAlgorithmRun`, `HierarchicalAlgorithmRun_Siletti` |
| SEA-AD | `SEA-AD_CorrelationAlgorithmRun`, `SEA-AD_HierarchicalAlgorithmRun`, `DeepGenerativeMapping` |
| BG Consensus | `HierarchicalAlgorithmRun`, `CorrelationAlgorithmRun` |

## Limits

- File upload: **2 GB max**, ~150K cells through web
- No authentication required (anonymous access)
- Files deleted after 1 week
