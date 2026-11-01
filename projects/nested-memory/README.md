# Nested Memory

A selected code and concept showcase from work on LZ: retrieve useful information across short-term, mid-term, and long-term memory while keeping its source and status visible.

The practical problem is familiar in business: a recent note, an active project summary, and an older decision may all matter to the same question. Searching only recent files can miss the decision that explains the current work.

## What the underlying work explores

- Search across memory layers and nested project folders, including older records.
- Return a relevant passage with its source, date when known, and review status.
- Keep superseded or rejected records out of ordinary active recall.
- Keep historical evidence and pending candidates visibly distinct from current information.
- Filter records marked local-only before selecting context to send beyond the local search.
- Bound the amount of retrieved context so a useful passage can fit into a larger workflow.

These capabilities were identified by inspecting the implementation and its synthetic test cases. This showcase does not establish production readiness or provide a security assessment.

## Selected original code

[`selected_helpers.mjs`](selected_helpers.mjs) publishes two small helper functions from the original implementation. Their function definitions are unchanged; a file comment and named exports were added to make this selection understandable and importable on its own.

- `localOnlyRecord(record)` checks nested objects for either supported local-only flag. A nested local-only marker marks the containing record local-only; a child's explicit `false` cannot override that boundary. Malformed present flags and the traversal limit also produce a local-only result.
- `excerptFor(document, words, maxChars)` chooses a short passage near matching query words, rather than always showing the beginning of a long document. It expects prepared `text` and `normalized` strings, normalized query words, and a valid character limit supplied by its caller.

Neither function reads files, calls a model, connects to an account, or includes real memory records. The privacy helper expects ordinary JSON-like data. A `false` result means no supported local-only marker was detected; it does not grant permission to publish a record. The excerpt helper formats text already supplied to it and performs no privacy checks itself. Filter first, then excerpt.

A separate synthetic demonstration uses fictional business records to illustrate these helpers in context. That demonstration is newly written showcase code, separate from the original excerpts.

## Fictional business example

Consider an invented workshop preparing an equipment inspection:

| Layer | Example record | Why it matters |
| --- | --- | --- |
| Short-term | Today's note: inspection checklist needs revision. | The immediate task. |
| Mid-term | Active project: replace the inspection checklist this month. | The current plan. |
| Long-term, inside a project folder | An earlier decision requires two reviewers before approval. | An older constraint that remains relevant. |

A query about the inspection checklist should find the older decision as well as the recent note. Each result should retain its source and status. A retrieved sentence is evidence to review; it does not authorize an action.

All example organizations, tasks, and records in this showcase are fictional.

## Run the fictional example

From the repository root:

```sh
node projects/nested-memory/demo.mjs "inspection checklist"
```

`demo.mjs` is a newly written in-memory keyword-search example using the original selected helpers and only the invented records in `sample_records.json`. Nested folder paths are source labels in this example; it does not traverse a real memory directory. It excludes the synthetic superseded and local-only records before ranking and keeps historical evidence labeled. It requires no packages, API credentials, model, or network connection.

The demonstration deliberately uses a simple match count instead of the private engine's ranking and context orchestration. Its filtering is instructional; input classification, authentication, and integration remain the caller's responsibility.

## Scope

The release contains only the two original helpers identified above and the separately identified synthetic teaching example. The complete memory engine, indexing and ranking implementation, compression system, orchestration, real memory records, personal conversations, identity material, account configuration, and live integrations remain private.

Deterministic keyword retrieval can miss paraphrases or return irrelevant matches. A source date may be unknown. Local-only flags require correctly classified inputs and enforcement by the calling application; the concept alone is not an access-control system. Search results still require human judgment.
