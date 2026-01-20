import re
from datetime import datetime

# Wyrażenie regularne dla daty w formacie dd-mm-yyyy lub dd/mm/yyyy
pattern = re.compile(r"^(0[1-9]|[12]\d|3[01])([-/])(0[1-9]|1[0-2])\2(\d{4})$")

months = {
  1: "styczeń",
  2: "luty",
  3: "marzec",
  4: "kwiecień",
  5: "maj",
  6: "czerwiec",
  7: "lipiec",
  8: "sierpień",
  9: "wrzesień",
  10: "październik",
  11: "listopad",
  12: "grudzień",
}

date_input = input("Podaj datę w formacie dd-mm-yyyy lub dd/mm/yyyy: ")

match = pattern.match(date_input)
if match:
  day, sep, month, year = match.groups()
  day = int(day)
  month = int(month)
  year = int(year)
  try:
    # Sprawdź, czy data jest rzeczywista
    datetime(year, month, day)
    print(f"Miesiąc: {months[month]}")
  except ValueError:
    print("Niepoprawna data")
else:
  print("Niepoprawny format daty")
