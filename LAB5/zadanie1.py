from typing import NoReturn


def convert_number() -> NoReturn:
  bases = {2, 8, 10, 16}
  base = 0
  while base not in bases:
    try:
      base = int(input("Enter base (2, 8, 10, 16): "))
      if base not in bases:
        print("Invalid base. Please choose 2, 8, 10, or 16.")
    except ValueError:
      print("Please enter a valid integer for base.")

  number_str = input(f"Enter number in base {base}: ")
  try:
    number = int(number_str, base)
    print(f"Binary: {bin(number)}")
    print(f"Octal: {oct(number)}")
    print(f"Decimal: {number}")
    print(f"Hexadecimal: {hex(number)}")
  except ValueError:
    print("Invalid number for the given base.")


if __name__ == "__main__":
  convert_number()
