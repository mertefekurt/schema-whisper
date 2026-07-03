from __future__ import annotations

import argparse
from pathlib import Path

from schema_whisper.core import infer_schema, load_jsonl, render_json_schema, render_table


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Infer a practical JSON schema from JSONL records.")
    parser.add_argument("jsonl", type=Path)
    parser.add_argument("--json-schema", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    profiles = infer_schema(load_jsonl(args.jsonl))
    print(render_json_schema(profiles) if args.json_schema else render_table(profiles), end="")
    return 0
