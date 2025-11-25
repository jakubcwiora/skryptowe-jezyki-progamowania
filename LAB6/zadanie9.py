class Employee:
  """Task 9: Employee class with save/load."""

  def __init__(self, name: str, age: int, salary: float):
    self.name = name
    self.age = age
    self.salary = salary

  def save_to_file(self, filename: str):
    try:
      with open(filename, "w") as f:
        f.write(f"{self.name}\n{self.age}\n{self.salary}\n")
      print(f"Saved to {filename}")
    except Exception as e:
      print(f"Save error: {e}")

  @classmethod
  def load_from_file(cls, filename: str):
    try:
      with open(filename, "r") as f:
        lines = f.readlines()
        name = lines[0].strip()
        age = int(lines[1].strip())
        salary = float(lines[2].strip())
      return cls(name, age, salary)
    except FileNotFoundError as e:
      print(f"File not found: {e}")
      raise
    except (ValueError, IndexError) as e:
      print(f"Invalid data: {e}")
      raise


def main():
  emp = Employee("John", 30, 50000.0)
  emp.save_to_file("employee.txt")
  loaded_emp = Employee.load_from_file("employee.txt")
  print(f"Loaded: {loaded_emp.name}, {loaded_emp.age}, {loaded_emp.salary}")


if __name__ == "__main__":
  main()
