import shutil
from pathlib import Path
from typing import Tuple


def test_copy(base: Path) -> Tuple[Path, Path, Path]:
  src_dir = base / "src"
  dst_dir = base / "dst"
  src_dir.mkdir(parents=True, exist_ok=True)
  if dst_dir.exists():
    shutil.rmtree(dst_dir)

  src_file = src_dir / "example.txt"
  src_file.write_text("original\n", encoding="utf-8")

  # 1) destination directory exists and file does not exist
  dst_dir.mkdir(parents=True, exist_ok=True)
  dst_file = dst_dir / "example.txt"
  if dst_file.exists():
    dst_file.unlink()
  shutil.copy(str(src_file), str(dst_file))
  print(" - copy when target does not exist: success")

  # 2) target exists -> will be overwritten
  dst_file.write_text("old content\n", encoding="utf-8")
  shutil.copy(str(src_file), str(dst_file))
  print(" - copy when target exists: overwritten")

  # 3) target directory does not exist
  shutil.rmtree(dst_dir)
  try:
    shutil.copy(str(src_file), str(dst_file))
    print(" - copy when target directory missing: unexpectedly succeeded")
  except FileNotFoundError as ex:
    print(
      " - copy when target directory missing: raised FileNotFoundError as expected:", ex
    )

  return src_file, dst_file, dst_dir


def main() -> None:
  print("Zadanie 7 demonstration:")
  base = Path("demo_outputs/zadanie7")
  base.mkdir(parents=True, exist_ok=True)
  test_copy(base)


if __name__ == "__main__":
  main()
