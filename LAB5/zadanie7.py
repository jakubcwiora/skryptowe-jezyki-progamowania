import math
from typing import NoReturn


def trigonometric_identity_check() -> NoReturn:
  for angle_deg in range(0, 91):
    angle_rad = math.radians(angle_deg)
    sin_sq = math.sin(angle_rad) ** 2
    cos_sq = math.cos(angle_rad) ** 2
    identity = sin_sq + cos_sq
    print(f"Angle {angle_deg}°: sin² + cos² = {identity} (should be ~1.0)")
    if not math.isclose(identity, 1.0, abs_tol=1e-10):
      print(f"Identity fails for {angle_deg}°")


if __name__ == "__main__":
  trigonometric_identity_check()
