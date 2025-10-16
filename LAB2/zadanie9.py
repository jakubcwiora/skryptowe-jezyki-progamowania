import calendar


def printCalendar():
  year = int(input("Podaj rok: "))
  month = int(input("Podaj miesiąc: "))
  print(calendar.month(year, month))
  
printCalendar()