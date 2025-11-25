import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List


@dataclass
class DemoObject:
  items: List[int]
  value: int
  name: str

  def to_json_file(self, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
      with path.open("w", encoding="utf-8") as fh:
        json.dump(asdict(self), fh, indent=2)
      print(f"Saved object to {path}")
    except OSError as ex:
      print("Error saving object:", ex)
      raise

  @classmethod
  def from_json_file(cls, path: Path) -> "DemoObject":
    try:
      with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
      return cls(items=data["items"], value=int(data["value"]), name=str(data["name"]))
    except FileNotFoundError:
      print("File not found when trying to load object:", path)
      raise
    except (json.JSONDecodeError, KeyError, TypeError) as ex:
      print("Error decoding or parsing JSON:", ex)
      raise


def main() -> None:
  p = Path("demo_outputs/zadanie9/demo_object.json")
  obj = DemoObject(items=[1, 2, 3], value=42, name="Alice")
  obj.to_json_file(p)
  loaded = DemoObject.from_json_file(p)
  print("Loaded object:", loaded)


if __name__ == "__main__":
  main()
