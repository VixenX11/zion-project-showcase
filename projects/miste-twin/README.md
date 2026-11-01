# Misté Twin

Misté Twin is a local professional-operations assistant project. The inspected implementation, named Clone Misté in its source, combines a browser dashboard, SQLite persistence, a configurable model adapter, and registered task handlers. It can organize dashboard items, prepare drafts, create local schedules, and record an audit trail.

A central design concern is durable workflow state. Completing or archiving work keeps its history. Removing an item creates a suppression record so that a later task does not quietly recreate it; restoration is an explicit step. The project also separates local organization and drafting from actions that require approval.

These patterns can be useful in business assistants where repeated recommendations, lost decisions, or unclear action boundaries create extra work.

## Selected source

[`approval_policy.py`](approval_policy.py) is an unchanged, standalone source excerpt from `agent/approval_policy.py`. It lists local action categories and categories requiring approval. Unknown action categories are denied by `authorize` because they are not in either permitted group.

The module illustrates policy classification only. It does not authenticate a person, collect an approval, execute an action, or prove that every application path enforces the policy. Its `approved` argument must be supplied by a trusted surrounding workflow.

This first showcase contains a selected module and an implementation overview. The full application, model integrations, dashboard assets, databases, profiles, imports, and operational records are outside this publication. No model or live workflow was invoked, and the full application was not tested as part of publication.
