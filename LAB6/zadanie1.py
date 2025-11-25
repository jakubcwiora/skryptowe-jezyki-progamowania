def case_division_by_zero() -> None:
  try:
    _ = 3 / 0
  except Exception as ex:
    print("case_division_by_zero: caught", type(ex).__name__, "-", ex)


def case_float_with_comma() -> None:
  try:
    _ = float("2,5")
  except Exception as ex:
    print("case_float_with_comma: caught", type(ex).__name__, "-", ex)


def case_valid_float() -> None:
  try:
    value = float("2.5")
    print("case_valid_float: success ->", value)
  except Exception as ex:
    print("case_valid_float: caught", type(ex).__name__, "-", ex)


def main() -> None:
  for func in (case_division_by_zero, case_float_with_comma, case_valid_float):  # type: ignore[arg-type]
    func()


if __name__ == "__main__":
  main()
