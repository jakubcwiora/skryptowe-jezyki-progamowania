class Student:
  def __init__(self, name: str = "", last_name: str = "", index: int = 0):
    print("Student constructor")
    self.name = name
    self.last_name = last_name
    self.index = index


class GraduateStudent(Student):
  def __init__(
    self, name: str = "", last_name: str = "", index: int = 0, thesis: str = ""
  ):
    print("GraduateStudent constructor")
    super().__init__(name, last_name, index)
    self.thesis = thesis


gs = GraduateStudent("Jane", "Doe", 123456, "AI Thesis")
