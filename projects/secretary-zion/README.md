# Secretary Zion

A selected concept showcase from work on LZ: an assistant and a person share an organized local workspace, with explicit records of what was actually saved.

## What the underlying work explores

- Organize tasks, notes, events, projects, and draft plans in a shared workspace.
- Apply a bounded group of changes as one transaction.
- Detect outdated edits using item versions instead of silently overwriting a newer change.
- Keep transaction history and support undo and redo within retained history.
- Recognize a repeated supported handoff request and return its existing receipt rather than create a duplicate.
- Distinguish a proposal, a successful local save, and a verified change in an external service.

These capabilities were identified by inspecting the implementation and its synthetic test cases. They are not a claim that an external account is connected or that a production deployment has been audited.

## Fictional business example

An invented design studio asks its assistant to prepare an equipment-review meeting and a follow-up task. The assistant first proposes the changes. A local transaction can save the meeting and task together and return a receipt. If another person has already edited the task, a version check can reject an outdated update.

Saving that meeting locally does not mean it was published to an external calendar. A real integration needs its own authorized operation and verified result.

All example organizations, meetings, and tasks in this showcase are fictional.

## Selected demonstration

[`versioned_task.mjs`](versioned_task.mjs) is a newly written, standard-library-only teaching example inspired by the version-check pattern. It updates a fictional task only when the expected version matches, returns a new task and an explicitly scoped in-memory receipt, and shows a stale update being rejected.

Run it from the repository root:

```sh
node projects/secretary-zion/versioned_task.mjs
```

The example neither persists a task nor saves it to an external service. It is not an excerpt of the complete Secretary service and does not implement the other underlying capabilities described above.

## Scope

This folder presents selected workflow ideas. It does not include the complete Secretary service, real workspace data, correspondence, personal modes or prompts, credentials, browser sessions, or account integrations. Any accompanying sample is a newly written teaching demonstration, not the original service.

The original persistence approach is designed around one writer inside one process. The concepts shown here do not by themselves provide a multi-user database, distributed locking, authentication, access control, or guaranteed external delivery. Retained history is bounded, so undo is not an unlimited archive.
