#!/usr/bin/env python3
"""yamlfmt - Format and validate YAML files."""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pip install pyyaml", file=sys.stderr)
    sys.exit(1)

def format_yaml(filepath: str, indent: int = 2, width: int = 120) -> str:
    """Load and re-dump YAML with consistent formatting."""
    path = Path(filepath)
    data = yaml.safe_load(path.read_text())
    return yaml.dump(data, default_flow_style=False, indent=indent, width=width, sort_keys=False)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Format YAML files")
    parser.add_argument("files", nargs="+")
    parser.add_argument("-i", "--in-place", action="store_true")
    parser.add_argument("--indent", type=int, default=2)
    args = parser.parse_args()

    for f in args.files:
        formatted = format_yaml(f, indent=args.indent)
        if args.in_place:
            Path(f).write_text(formatted)
            print(f"Formatted: {f}")
        else:
            print(formatted)

if __name__ == "__main__":
    main()
