import random


def generate_and_save_numbers(n: int, a: float, b: float, filename: str):
  """Task 8: Generate and save numbers."""
  try:
    numbers = [random.uniform(a, b) for _ in range(n)]
    with open(filename, "w") as f:
      for num in numbers:
        f.write(f"{num}\n")
    print(f"Saved {n} numbers to {filename}")
  except ValueError as e:
    print(f"Invalid range: {e}")
  except Exception as e:
    print(f"Error: {e}")


def main():
  generate_and_save_numbers(5, 1.0, 10.0, "numbers.txt")


if __name__ == "__main__":
  main()
