class Student:
  def __init__(self, name: str, last_name: str, index: int):
    self.name = name
    self.last_name = last_name
    self.index = index


s = Student("Joe", "Doe", 111111)
print(s.__dict__)  # {'name': 'Joe', 'last_name': 'Doe', 'index': 111111}
