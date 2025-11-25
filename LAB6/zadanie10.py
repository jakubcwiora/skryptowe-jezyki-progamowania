import struct


def convert_text_to_binary(input_file: str, output_file: str):
  """Task 10: Convert text numbers to binary."""
  try:
    numbers = []
    with open(input_file, "r") as f:
      for line in f:
        numbers.append(float(line.strip()))
    with open(output_file, "wb") as f:
      for num in numbers:
        f.write(struct.pack("d", num))
    print(f"Converted {len(numbers)} numbers to binary in {output_file}")
  except FileNotFoundError as e:
    print(f"Input file not found: {e}")
  except ValueError as e:
    print(f"Invalid number: {e}")
  except Exception as e:
    print(f"Error: {e}")


def main():
  # First generate numbers if needed
  import random

  numbers = [random.uniform(1.0, 10.0) for _ in range(5)]
  with open("numbers.txt", "w") as f:
    for num in numbers:
      f.write(f"{num}\n")
  convert_text_to_binary("numbers.txt", "numbers.bin")


if __name__ == "__main__":
  main()
