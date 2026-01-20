import re

with open("numery.txt", "r", encoding="utf-8") as file:
  numbers = file.readlines()

pattern = re.compile(r"^(\+48|0048)")

for number in numbers:
  number = number.strip()
  if pattern.match(number):
    print(number)
