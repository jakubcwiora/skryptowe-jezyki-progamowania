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
    print(
      "Hello! I'm "
      + self.name
      + " "
      + self.last_name
      + " with index "
      + str(self.index)
    )

  def average_mark(self) -> float:
    if self.marks:
      return sum(self.marks) / len(self.marks)
    return 0.0

  def set_index(self, index: int) -> None:
    self.index = index


# Create several instances
s1 = Student()
s2 = Student()
s3 = Student()

print("s1.quantity:", s1.quantity)
print("s2.quantity:", s2.quantity)
print("s3.quantity:", s3.quantity)
print("Student.quantity:", Student.quantity)
