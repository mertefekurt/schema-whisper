# Schema Whisper

Infer a practical JSON schema from messy JSONL examples.

![Schema Whisper cover](assets/readme-cover.svg)

## Why it is useful

When an event stream has grown by habit, this gives you a first readable profile: fields, observed types, nulls, and a JSON Schema draft.

```bash
git clone https://github.com/mertefekurt/schema-whisper.git
cd schema-whisper
python -m pip install -e ".[dev]"
schema-whisper examples/events.jsonl
schema-whisper examples/events.jsonl --json-schema
```
