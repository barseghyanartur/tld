#!/usr/bin/env python3
import argparse
import fnmatch
import os
from pathlib import Path


def build_tree(
    path: Path,
    max_depth: int,
    ignore_patterns: list,
    whitelist_dirs: list,
    include_all: bool,
    root: Path,
    prefix: str = "",
) -> str:
    """
    Recursively build an ASCII tree up to max_depth, applying whitelist and
    ignore rules.
    """
    if max_depth < 0:
        return ""
    entries = sorted(
        path.iterdir(), key=lambda p: (p.is_file(), p.name.lower())
    )
    lines = []
    for i, entry in enumerate(entries):
        rel_path = entry.relative_to(root).as_posix()
        # Skip ignored patterns
        if any(fnmatch.fnmatch(rel_path, pat) for pat in ignore_patterns):
            continue
        # Enforce whitelist if not including all
        if (
            not include_all
            and whitelist_dirs
            and not any(
                rel_path.startswith(w.rstrip("/")) for w in whitelist_dirs
            )
        ):
            continue
        connector = "└── " if i == len(entries) - 1 else "├── "
        lines.append(f"{prefix}{connector}{entry.name}")
        # Recurse into directories
        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            subtree = build_tree(
                entry,
                max_depth - 1,
                ignore_patterns,
                whitelist_dirs,
                include_all,
                root,
                prefix + extension,
            )
            if subtree:
                lines += subtree.splitlines()
    return "\n".join(lines)


def detect_language(path: Path) -> str:
    """Map file suffix to Sphinx language."""
    mapping = {
        ".py": "python",
        ".js": "javascript",
        ".java": "java",
        ".md": "markdown",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".json": "json",
        ".sh": "bash",
        ".rst": "rst",
    }
    return mapping.get(path.suffix, "")


def main():
    p = argparse.ArgumentParser(
        description="Auto-generate a .rst with tree + literalinclude blocks"
    )
    p.add_argument(
        "-p",
        "--project-root",
        type=Path,
        default=Path("."),
        help="Path to your project directory",
    )
    p.add_argument(
        "-d",
        "--depth",
        type=int,
        default=10,
        help="How many levels deep to print in the tree",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("docs/source_tree.rst"),
        help="Where to write the generated .rst",
    )
    p.add_argument(
        "-e",
        "--ext",
        nargs="+",
        default=[".py", ".md", ".js", ".rst"],
        help="Which file extensions to include via literalinclude",
    )
    p.add_argument(
        "-i",
        "--ignore",
        nargs="+",
        default=["__pycache__", "*.pyc", "*.py,cover"],
        help="Ignore files or dirs matching these glob patterns (relative to "
        "project root)",
    )
    p.add_argument(
        "-w",
        "--whitelist",
        nargs="+",
        default=["src", "docs", "examples", "scripts"],
        help="Directories (relative to project root) to include "
        "unless --include-all is given",
    )
    p.add_argument(
        "--include-all",
        action="store_true",
        help="Include all files regardless of whitelist",
    )
    args = p.parse_args()

    root = args.project_root.resolve()
    ignore_patterns = args.ignore
    whitelist_dirs = args.whitelist
    include_all = args.include_all
    output = args.output.resolve()
    output_dir = output.parent.resolve()

    # Header + tree
    header = f"""Project source-tree
===================

Below is the layout of our project (to {args.depth} levels), followed by
the contents of each key file.

.. code-block:: bash
   :caption: Project directory layout

   {root.name}/
"""
    tree = build_tree(
        root,
        args.depth,
        ignore_patterns,
        whitelist_dirs,
        include_all,
        root,
        prefix="   ",
    )
    out = [header, tree, ""]

    # Walk and collect files
    for filepath in sorted(root.rglob("*")):
        if not filepath.is_file() or filepath.suffix not in args.ext:
            continue
        rel_path = filepath.relative_to(root).as_posix()
        # Skip ignored
        if any(fnmatch.fnmatch(rel_path, pat) for pat in ignore_patterns):
            continue
        # Enforce whitelist
        if (
            not include_all
            and whitelist_dirs
            and not any(
                rel_path.startswith(w.rstrip("/")) for w in whitelist_dirs
            )
        ):
            continue

        # Compute include path relative to output_dir
        include_path = os.path.relpath(filepath, output_dir).replace(
            os.sep, "/"
        )
        title = rel_path
        underline = "-" * len(title)
        lang = detect_language(filepath)
        out += [
            title,
            underline,
            "",
            f".. literalinclude:: {include_path}",
            f"   :language: {lang}" if lang else "",
            f"   :caption: {rel_path}",
            # "   :linenos:",
            "",
        ]

    # Write output
    args.output.write_text("\n".join(line for line in out if line is not None))
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
