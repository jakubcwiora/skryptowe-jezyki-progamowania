from pathlib import Path
from typing import Optional


def print_tree(
  path: Path, prefix: str = "", max_depth: Optional[int] = 3, _depth: int = 0
) -> None:
  """
  Print a simple tree of files and directories starting at `path`.
  `max_depth` limits recursion depth; None means unlimited.
  """
  if max_depth is not None and _depth > max_depth:
    return
  try:
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
  except Exception as ex:
    print(prefix + f"[error reading {path}: {ex}]")
    return

  for i, entry in enumerate(entries):
    is_last = i == len(entries) - 1
    connector = "└── " if is_last else "├── "
    print(prefix + connector + entry.name)
    if entry.is_dir():
      extension = "    " if is_last else "│   "
      print_tree(entry, prefix + extension, max_depth, _depth + 1)


def main() -> None:
  print("Zadanie 6 demonstration: tree of current directory (depth 2)")
  print(".")
  print_tree(Path("."), max_depth=2)


if __name__ == "__main__":
  main()
