from typing import List


class Student:
  quantity = 0

  def __init__(self):
    self.name = ""
    self.last_name = ""
    self.marks = []
    self.index = 0
    Student.quantity += 1

  def give_name(self, name: str, last_name: str) -> None:
    self.name = name
    self.last_name = last_name

  def give_mark(self, mark: int) -> None:
    self.marks.append(mark)

  def get_marks(self) -> List[int]:
    return self.marks

  def say_hello(self) -> None:
    if self._is_name_valid():
      print(
        "Hello! I'm "
        + self.name
        + " "
        + self.last_name
        + " with index "
        + str(self.index)
      )
    else:
      print("Name not set properly.")

  def average_mark(self) -> float:
    if self.marks:
      return sum(self.marks) / len(self.marks)
    return 0.0

  def set_index(self, index: int) -> None:
    self.index = index

  def _is_name_valid(self) -> bool:
    return self.name != "" and self.last_name != ""


# Example usage
s = Student()
s.say_hello()  # Name not set properly.
s.give_name("Jane", "Doe")
s.say_hello()  # Hello! I'm Jane Doe with index 0

# Try to call private method outside class (not recommended, but for demonstration)
try:
  print(s._is_name_valid())  # True
except AttributeError:
  print("Cannot access private method directly")
