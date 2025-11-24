from datetime import date

currentDate = date.today() # Pobieramy dzisiejszą date i wypisujemy
                           # w różnych formatach
print(currentDate.strftime('%d/%m/%y'))
print(currentDate.strftime('%m/%d/%y'))
print(currentDate.strftime('%y/%m/%d'))

