import random
import math


def triangle_area() -> float:
  sides = [random.randint(3, 10) for _ in range(3)]
  a, b, c = sides
  print(f"Generated sides: {a}, {b}, {c}")
  if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Can form a triangle. Area: {area}")
    return area
  else:
    print("Cannot form a triangle.")
    return 0.0


if __name__ == "__main__":
  triangle_area()
