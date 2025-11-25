from pathlib import Path
import json
from typing import Dict

DEMO_DIR = Path("demo_outputs")
DEMO_DIR.mkdir(exist_ok=True)


def test_open_modes() -> Dict[str, Dict[str, str]]:
  test_dir = DEMO_DIR / "open_modes"
  test_dir.mkdir(parents=True, exist_ok=True)
  existing = test_dir / "existing.txt"
  existing.write_text("existing content\n", encoding="utf-8")

  results: Dict[str, Dict[str, str]] = {}
  for mode in ("r", "w", "a", "x"):
    results[mode] = {}
    # try writing to existing file
    try:
      with open(existing, mode) as fh:
        fh.write("try write\n")
      results[mode]["existing"] = "write succeeded"
    except Exception as ex:
      results[mode]["existing"] = f"error: {type(ex).__name__}: {ex}"

    # try writing to a non-existing file
    nonexist = test_dir / f"nonexist_{mode}.txt"
    if nonexist.exists():
      nonexist.unlink()
    try:
      with open(nonexist, mode) as fh:
        fh.write("try write\n")
      results[mode]["nonexist"] = "write succeeded (created or opened)"
    except Exception as ex:
      results[mode]["nonexist"] = f"error: {type(ex).__name__}: {ex}"

  out = DEMO_DIR / "open_modes_results.json"
  out.write_text(json.dumps(results, indent=2), encoding="utf-8")
  print("Results written to", out)
  return results


def main() -> None:
  test_open_modes()


if __name__ == "__main__":
  main()
