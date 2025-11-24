def get_bit(number: int, bit_index: int) -> int:
  if not isinstance(number, int):
    return TypeError("Number must be an integer.")
  if not isinstance(bit_index, int):
    return TypeError("Bit index must be an integer.")
  if not (0 <= number <= 255):
    raise ValueError("Number must be between 0 and 255.")
  if bit_index < 0 or bit_index > 7:
    raise ValueError("Bit index must be between 0 and 7.")
  return (number >> bit_index) & 1


if __name__ == "__main__":
  try:
    num = int(input("Enter number (0-255): "))
    bit = int(input("Enter bit index (0-7): "))
    result = get_bit(num, bit)
    print(f"Bit at index {bit} in {num} is {result}")
  except ValueError as e:
    print(e)
