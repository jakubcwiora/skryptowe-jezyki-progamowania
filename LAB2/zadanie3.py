from datetime import date

currentDate = date.today()
print(currentDate.strftime('%d/%m/%y'))
print(currentDate.strftime('%m/%d/%y'))
print(currentDate.strftime('%y/%m/%d'))