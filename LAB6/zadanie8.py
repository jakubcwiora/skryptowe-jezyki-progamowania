import random
from pathlib import Path
from typing import List


def generate_random_numbers(n: int, a: int, b: int, filename: Path) -> List[int]:
  if n <= 0:
    raise ValueError("n must be positive")
  if a > b:
    raise ValueError("a must be <= b")
  numbers = [random.randint(a, b) for _ in range(n)]
  filename.parent.mkdir(parents=True, exist_ok=True)
  filename.write_text("\n".join(str(x) for x in numbers) + "\n", encoding="utf-8")
  print(f"Wrote {n} numbers to {filename}")
  return numbers


def main() -> None:
  out = Path("demo_outputs/zadanie8/numbers.txt")
  generate_random_numbers(10, 1, 100, out)


if __name__ == "__main__":
  main()
