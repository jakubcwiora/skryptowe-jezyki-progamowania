from typing import List


class Student:
  _next_index: int = 1

  def __init__(self):
    self.name = ""
    self.last_name = ""
    self.marks = []
    self.index = None

  def give_name(self, name: str, last_name: str) -> None:
    self.name = name
    self.last_name = last_name

  def give_mark(self, mark: int) -> None:
    self.marks.append(mark)

  def give_index(self) -> int:
    self.index = self._next_index
    Student._next_index += 1

  def get_marks(self) -> List[int]:
    return self.marks

  def say_hello(self) -> None:
    print(
      "Hello! I'm " + self.name + " " + self.last_name + "\n my index number is: ",
      self.index,
    )

  def get_mean_grade(self) -> float:
    return sum(self.marks) / len(self.marks)


s = Student()
s.give_name("Jane", "Doe")
s.give_mark(5)  # wywołanie sposób 1
Student.give_mark(s, 3)  # wywołanie sposób 2
s.give_index()
print(s.get_marks())
s.say_hello()
