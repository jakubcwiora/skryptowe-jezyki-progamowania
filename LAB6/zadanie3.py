from typing import Optional


def compute_division(divisor: int) -> Optional[float]:
  try:
    result = 10 / divisor
    print("  try: computed result =", result)
  except ZeroDivisionError:
    print("  except: caught division by zero")
    return None
  else:
    print("  else: executed because no exception occurred")
  finally:
    print("  finally: always executes")
  return result


def main() -> None:
  print("Zadanie 3 demonstration:")
  print("- call with divisor=2")
  compute_division(2)
  print("- call with divisor=0")
  compute_division(0)


if __name__ == "__main__":
  main()
