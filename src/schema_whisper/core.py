from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class FieldProfile:
    name: str
    types: tuple[str, ...]
    required: bool
    examples: tuple[str, ...]


def json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "unknown"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError("each JSONL row must be an object")
            records.append(value)
    return records


def infer_schema(records: list[dict[str, Any]]) -> list[FieldProfile]:
    field_names = sorted({key for record in records for key in record})
    profiles: list[FieldProfile] = []
    total = len(records)
    for name in field_names:
        seen = [record[name] for record in records if name in record]
        types = tuple(sorted({json_type(value) for value in seen}))
        examples = tuple(str(value)[:60] for value in seen[:3])
        profiles.append(FieldProfile(name, types, len(seen) == total, examples))
    return profiles


def render_table(profiles: list[FieldProfile]) -> str:
    lines = ["field\ttypes\trequired\texamples"]
    for profile in profiles:
        required = "yes" if profile.required else "no"
        lines.append(f"{profile.name}\t{','.join(profile.types)}\t{required}\t{'; '.join(profile.examples)}")
    return "\n".join(lines) + "\n"


def render_json_schema(profiles: list[FieldProfile]) -> str:
    schema = {"type": "object", "properties": {}, "required": []}
    for profile in profiles:
        schema["properties"][profile.name] = {"type": list(profile.types)}
        if profile.required:
            schema["required"].append(profile.name)
    return json.dumps(schema, indent=2, sort_keys=True)
