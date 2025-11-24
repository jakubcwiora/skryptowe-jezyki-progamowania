import math
from typing import NoReturn


def ladder_height() -> NoReturn:
  length = float(input("Enter ladder length: "))
  angle_deg = float(input("Enter angle in degrees: "))
  angle_rad = math.radians(angle_deg)
  height = length * math.sin(angle_rad)
  print(f"The height reached by the ladder is: {height}")


if __name__ == "__main__":
  ladder_height()
