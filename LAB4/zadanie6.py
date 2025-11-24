class Student:
  quantity = 0

  def __init__(self, name: str = "", last_name: str = "", index: int = 0):
    self.name = name
    self.last_name = last_name
    self.marks = []
    self.index = index
    Student.quantity += 1

  def __eq__(self, o: object) -> bool:
    if isinstance(o, Student):
      return self.index == o.index
    return False

  def __ne__(self, o: object) -> bool:
    return not self.__eq__(o)

  def __lt__(self, o: object) -> bool:
    if isinstance(o, Student):
      return self.index < o.index
    return False

  def __gt__(self, o: object) -> bool:
    if isinstance(o, Student):
      return self.index > o.index
    return False

  def __le__(self, o: object) -> bool:
    return self.__eq__(o) or self.__lt__(o)

  def __ge__(self, o: object) -> bool:
    return self.__eq__(o) or self.__gt__(o)


# Example usage
s1 = Student("Joe", "Doe", 111111)
s2 = Student("Jane", "Key", 222222)

print(s1 == s2)  # False
print(s1 != s2)  # True
print(s1 < s2)  # True
print(s1 > s2)  # False
print(s1 <= s2)  # True
print(s1 >= s2)  # False
