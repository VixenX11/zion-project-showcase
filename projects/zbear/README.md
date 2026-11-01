# Z-Bear

Z-Bear is an elementary education AI tutor project intended for grades K–5. Its design goals include guided questioning, support for foundational learning, teacher involvement, and clear explanations for families.

The inspected Python prototype defines structured lesson plans and instructional stages. Its curriculum-agnostic design separates teacher- or district-authored lesson content from the instructional flow. Stages can represent a warm-up, mini-lesson, guided practice, a check-for-understanding pause (`cfu_pause`), independent practice, an exit ticket, and other classroom activities. Each stage can carry timing, a title, a prompt, key points, materials, and notes.

The current prototype and code selection focus on lesson-data structures for educators and developers exploring how to organize instructional interactions.

## Selected source

[`lesson_stage.py`](lesson_stage.py) contains the original `ALLOWED_STAGE_TYPES` set and `Stage` dataclass extracted from `python/lesson_plan_schema.py`. Those definitions are unchanged; imports are adjusted for the standalone excerpt. The complete lesson-plan structure, validator, runner, and model integrations are outside this showcase. The excerpt itself does not enforce the allowed-stage set or validate instructional content.

[`stage_example.py`](stage_example.py) is a newly written, fictional example showing how to construct a check-for-understanding stage. It uses synthetic content and contains no student records. It does not invoke a model, teach a live learner, or measure understanding.

Run it with Python 3 from the repository root:

```sh
python projects/zbear/stage_example.py
```

## Rights

The original copyright and rights notice is preserved in [`NOTICE.md`](NOTICE.md). All rights reserved. Public visibility of this selected showcase does not grant a general license to the full project.
