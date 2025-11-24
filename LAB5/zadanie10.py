import math
import sys
from typing import NoReturn


def test_math_functions() -> NoReturn:
  a = float(input("Enter a float number a: "))
  print(f"math.trunc({a}) = {math.trunc(a)}")
  print(f"math.floor({a}) = {math.floor(a)}")
  print(f"math.ceil({a}) = {math.ceil(a)}")

  version = sys.version_info
  print(f"Python version: {version.major}.{version.minor}")
  if version >= (3, 9):
    b = int(input("Enter an integer b: "))
    print(f"math.lcm({int(a)}, {b}) = {math.lcm(int(a), b)}")
    print(f"math.gcd({int(a)}, {b}) = {math.gcd(int(a), b)}")
  else:
    print("Python version < 3.9, skipping lcm and gcd.")

  print(f"math.fabs in math: {hasattr(math, 'fabs')}")
  print("abs is built-in, not in math module.")


if __name__ == "__main__":
  test_math_functions()
