def basicOperatorsOnIntegers():
  # Wczytujemy dwie zmienne jako liczby
  try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    
    print("a + b = ", a + b)
    print("a - b = ", a - b)
    print("a * b = ", a * b)
    print("a / b = ", a / b)
    print("a // b = ", a // b)
    print("a % b = ", a % b)
    print("a ** b = ", a ** b)
    
  except ValueError:
    print("Błąd przy wczytywaniu liczb")
  except ZeroDivisionError:
    print("Nie wolno dzielić przez zero !!!")
  
  
basicOperatorsOnIntegers()