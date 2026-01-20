import re

with open("numery.txt", "r", encoding="utf-8") as file:
  numbers = [line.strip() for line in file.readlines()]

# Wyrażenia regularne dla walidacji:
# 1. +48 XXX XXX XXX (np. +48 123 456 789)
pattern1 = re.compile(r"^\+48 \d{3} \d{3} \d{3}$")
# 2. 0048-XXX-XXX-XXX (np. 0048-123-456-789)
pattern2 = re.compile(r"^0048-\d{3}-\d{3}-\d{3}$")
# 3. +48XXXXXXXXX (np. +48123456789)
pattern3 = re.compile(r"^\+48\d{9}$")
# 4. 0048XXXXXXXXX (np. 0048123456789)
pattern4 = re.compile(r"^0048\d{9}$")
# 5. Inny format, np. +48 XXX-XXX-XXX
pattern5 = re.compile(r"^\+48 \d{3}-\d{3}-\d{3}$")

patterns = [pattern1, pattern2, pattern3, pattern4, pattern5]
counts = [0] * len(patterns)

for number in numbers:
  for i, pattern in enumerate(patterns):
    if pattern.match(number):
      counts[i] += 1
      break  # Zakładamy, że każdy numer pasuje tylko do jednego formatu

for i, count in enumerate(counts, 1):
  print(f"Format {i}: {count} numerów")
