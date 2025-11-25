from typing import NoReturn


def raise_generic() -> NoReturn:
  raise Exception("Generic exception from raise_generic")


def raise_value() -> NoReturn:
  raise ValueError("ValueError from raise_value")


def main() -> None:
  print("Zadanie 2 demonstration:")

  try:
    raise_generic()
  except ValueError as ex:
    print("Caught ValueError (unexpected):", ex)
  except Exception as ex:
    print("Caught Exception as expected:", type(ex).__name__, "-", ex)

  try:
    raise_value()
  except ValueError as ex:
    print("Caught ValueError as expected:", ex)
  except Exception as ex:
    print("Caught Exception (fallback):", type(ex).__name__, "-", ex)


if __name__ == "__main__":
  main()
