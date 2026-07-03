from __future__ import annotations

import json

from schema_whisper.cli import main
from schema_whisper.core import infer_schema, json_type, render_json_schema, render_table


def test_json_type_detects_bool_before_int() -> None:
    assert json_type(True) == "boolean"


def test_infers_optional_field() -> None:
    profiles = infer_schema([{"a": 1}, {}])
    assert profiles[0].required is False


def test_mixed_types_are_kept() -> None:
    profiles = infer_schema([{"score": 1}, {"score": "1"}])
    assert profiles[0].types == ("integer", "string")


def test_table_contains_field_name() -> None:
    assert "score" in render_table(infer_schema([{"score": 1}]))


def test_json_schema_required_list() -> None:
    schema = json.loads(render_json_schema(infer_schema([{"a": 1}, {"a": 2}])))
    assert schema["required"] == ["a"]


def test_cli_help(capsys) -> None:
    try:
        main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0
    assert "schema" in capsys.readouterr().out.lower()
