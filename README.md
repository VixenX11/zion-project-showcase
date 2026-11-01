# Zion Project Showcase

Selected work by **VixenX11** on practical assistants, local memory, and small productivity tools.

This portfolio shares project ideas and deliberately small code selections. The featured work explores finding older decisions when they matter, keeping assistant actions reviewable, and building useful local tools.

| Project | Practical focus | Included here |
| --- | --- | --- |
| [Nested Memory](projects/nested-memory/) | Find relevant context across memory layers and nested project folders. | Design overview, two original retrieval helpers, and a new example using fictional records. |
| [Secretary Zion](projects/secretary-zion/) | Organize work with explicit state and version checks. | Workflow overview and a new version-check demonstration. |
| [M4Mark](projects/m4mark/) | Android recording and manual on-device transcription. | Project overview and the original pause-aware recording clock. |
| [Kawaii Cat Timer](projects/cat-timer/) | A small desktop countdown widget. | Project overview and original time-entry helpers. |
| [Misté Twin](projects/miste-twin/) | Local assistant workflows with clear action boundaries. | Project overview and the original action-classification module. |

The original code excerpts and newly written demonstrations are identified in each project. These selections are not complete applications or downloadable product releases. Descriptions of the larger projects are based on inspected source; the full applications were not rebuilt for this showcase.

## Explore the examples

With Node.js installed, run these commands from this repository's root. The demonstrations use only the standard library, fictional data, and local computation.

```sh
node projects/nested-memory/demo.mjs "inspection checklist"
node projects/secretary-zion/versioned_task.mjs
```

The Python excerpts can be read or imported independently. The Kotlin clock is a standalone class intended for integration with a caller-supplied clock.

## Publication scope

LZ's full engine, orchestration, memory encoding, complete ranking implementation, private prompts, real memory records, and account integrations remain outside this repository. Source archives, operational databases, private conversation history, credentials, artwork, and alarm audio are not included.

## Rights and business inquiries

This is a public portfolio with rights reserved, not an open-source release. No broad reuse license is granted here. See [RIGHTS.md](RIGHTS.md) for the publication notice and licensing inquiries.
