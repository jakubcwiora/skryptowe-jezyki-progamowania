from datetime import date, timedelta

born = date(2006, 8, 5)
today = date.today()
age = today - born
print(f"Mam {(age.days/365).__round__(1)} lat!!!")

