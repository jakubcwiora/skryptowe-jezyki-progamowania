from pathlib import Path


def safe_open_read(path: Path) -> str:
  try:
    with path.open("r", encoding="utf-8") as fh:
      return fh.read()
  except FileNotFoundError as ex:
    raise FileNotFoundError(f"File not found: {path}") from ex


def demonstrate_errors() -> None:
  missing = Path("this_file_does_not_exist.txt")
  try:
    _ = safe_open_read(missing)
  except FileNotFoundError as ex:
    print(" - Opening non-existent file raised:", type(ex).__name__, "-", ex)

  p = Path("zadanie4_demo.txt")
  p.write_text("hello\n", encoding="utf-8")
  try:
    fh = p.open("r", encoding="utf-8")
    try:
      fh.write("attempt to write\n")
    except Exception as ex:
      print(" - Writing to file opened in 'r' raised:", type(ex).__name__, "-", ex)
    finally:
      fh.close()
  finally:
    if p.exists():
      p.unlink()


def main() -> None:
  demonstrate_errors()


if __name__ == "__main__":
  main()
