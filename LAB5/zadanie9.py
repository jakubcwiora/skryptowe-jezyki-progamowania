def power_of_two(p: int) -> int:
  return 1 << p


if __name__ == "__main__":
  p = int(input("Enter exponent p: "))
  result = power_of_two(p)
  print(f"2^{p} = {result}")
