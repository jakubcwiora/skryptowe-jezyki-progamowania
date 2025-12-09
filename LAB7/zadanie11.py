import pytest
import re


# Funkcja z zadanie4
def find_female_names(names):
  pattern = re.compile(r"^[A-Z][a-z]*a$")
  return [name for name in names if pattern.match(name)]


# Funkcja z zadanie5 (uproszczona dla testów)
def find_polish_numbers(numbers):
  pattern = re.compile(r"^(\+48|0048)")
  return [num for num in numbers if pattern.match(num)]


# Testy dla find_female_names (skrót myślowy do imion zakończonych a 'a')
def test_find_female_names_normal():
  names = ["Anna", "Jan", "Maria"]
  result = find_female_names(names)
  assert result == ["Anna", "Maria"]


def test_find_female_names_no_matches():
  names = ["Jan", "Piotr", "Adam"]
  result = find_female_names(names)
  assert result == []


def test_find_female_names_mixed():
  names = ["anna", "Anna", "Jan", "maria"]
  result = find_female_names(names)
  assert result == ["Anna"]  # Tylko wielka litera na początku


# Testy dla find_polish_numbers
def test_find_polish_numbers_normal():
  numbers = ["+48 123", "0048 456", "123"]
  result = find_polish_numbers(numbers)
  assert result == ["+48 123", "0048 456"]


def test_find_polish_numbers_no_matches():
  numbers = ["123", "456", "+1 123"]
  result = find_polish_numbers(numbers)
  assert result == []


def test_find_polish_numbers_partial():
  numbers = ["+48abc", "+48123", "0048123"]
  result = find_polish_numbers(numbers)
  assert result == ["+48abc", "+48123", "0048123"]  # Zakładamy, że pasuje początek
