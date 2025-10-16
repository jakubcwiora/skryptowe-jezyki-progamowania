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
    
  except:
    print("Błąd przy wczytywaniu liczb")
  
  
  
basicOperatorsOnIntegers()