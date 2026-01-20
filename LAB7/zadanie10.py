import re

strings = ["apple", "box", "cat", "dog",
            "exy", "fox", "goat", "hey", "ice", "joy"]

# Kończące się na x lub y
print("Elementy kończące się na x lub y:")
for s in strings:
  if re.match(r".*[xy]$", s):
    print(s)

# Trzyznakowe zaczynające się od a
print("\nElementy trzyznakowe zaczynające się od a:")
for s in strings:
  if re.match(r"^a..$", s):
    print(s)

# Rozpoczynające się samogłoską
print("\nElementy rozpoczynające się samogłoską:")
for s in strings:
  if re.match(r"^[aeiouAEIOU]", s):
    print(s)
