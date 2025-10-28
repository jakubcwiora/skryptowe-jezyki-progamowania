def getNumbers() -> None:
  userInput = True
  numbers = set()
  while userInput:
    try:
      str_input = input("Podaj liczbę: ")
      userInput = float(str_input)
      numbers.add(userInput)
    except ValueError:
      userInput = True
      print("To nie liczba")
  
  print("Podane unikatowe liczby to: ", numbers)
  
getNumbers()
      