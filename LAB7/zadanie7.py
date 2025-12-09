import re

# Wyrażenie regularne dla Gmail: zaczyna się od małej litery, potem małe litery, cyfry, _, -, ., kończy się @gmail.com
pattern = re.compile(r"^[a-z][a-z0-9_.-]*@gmail\.com$")

# Przykład użycia
email = "example@gmail.com"
if pattern.match(email):
  print("Poprawny adres Gmail")
else:
  print("Niepoprawny adres Gmail")
