class Student:
  def __init__(self, name: str, last_name: str, index: int):
    self.name = name
    self.last_name = last_name
    self.index = index


# Default
s = Student("Joe", "Doe", 111111)
print(repr(s))  # <__main__.Student object at 0x...>
print(str(s))  # <__main__.Student object at 0x...>


# Add __repr__ and __str__
class Student:
  def __init__(self, name: str, last_name: str, index: int):
    self.name = name
    self.last_name = last_name
    self.index = index

  def __repr__(self) -> str:
    return f"Student.name('{self.name}') Student.last_name('{self.last_name}')"

  def __str__(self) -> str:
    return f"{self.name} {self.last_name} "


# Overloaded
s = Student("Joe", "Doe", 111111)
print(repr(s))  # Joe Doe
print(str(s))  # Doe Joe
