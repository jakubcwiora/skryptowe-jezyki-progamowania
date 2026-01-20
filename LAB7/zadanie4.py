import re

names = [
  "Anna",
  "Jan",
  "Maria",
  "Piotr",
  "Katarzyna",
  "Tomasz",
  "Ewa",
  "Michał",
  "Barbara",
  "Adam",
]

pattern = re.compile(r"^[A-Z][a-z]*a$")  # Wielka litera na początku, kończy się na 'a'

for name in names:
  if pattern.match(name):
    print(name)
