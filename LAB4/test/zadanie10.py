from LAB4.zadanie1 import (
  Student,
)


def test_get_mean_grade_empty():
  s = Student()
  assert s.get_mean_grade() == 0.0


def test_get_mean_grade_one_mark():
  s = Student()
  s.give_mark(5)
  assert s.get_mean_grade() == 5.0


def test_get_mean_grade_multiple_marks():
  s = Student()
  s.give_mark(4)
  s.give_mark(5)
  s.give_mark(6)
  assert s.get_mean_grade() == 5.0
