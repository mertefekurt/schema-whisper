<img src="assets/readme-cover.svg" alt="Schema Whisper cover" width="100%" />

# Schema Whisper

Infer practical JSON schemas from messy JSONL examples.

![stack](https://img.shields.io/badge/stack-Python-2563eb?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-16a34a?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-dc2626?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-7c3aed?style=flat-square)

| Question | Answer |
| --- | --- |
| What is it? | A focused Python utility for schema hygiene. |
| How does it run? | `schema-whisper` |
| Why keep it small? | Easier review, easier tests, fewer moving parts. |

## Command

```bash
python -m pip install -e ".[dev]"
schema-whisper examples/events.jsonl
```

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m schema_whisper --help
```
