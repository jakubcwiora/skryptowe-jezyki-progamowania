import os


def print_directory_tree(directory: str, indent: str = "") -> None:
  try:
    entries = os.listdir(directory)
    for entry in entries:
      path = os.path.join(directory, entry)
      if os.path.isdir(path):
        print(f"{indent}Dir: {entry}")
        print_directory_tree(path, indent + "  ")
      else:
        print(f"{indent}File: {entry}")
  except PermissionError as e:
    print(f"Permission denied: {e}")
  except FileNotFoundError as e:
    print(f"Directory not found: {e}")


def main() -> None:
  print_directory_tree(".")


if __name__ == "__main__":
  main()
