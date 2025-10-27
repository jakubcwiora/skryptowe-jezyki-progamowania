def getList():
  list = []
  while len(list) < 10:
    try:
      num_string = input("Podaj liczbe: ")
      num = float(num_string) # Sprawdzamy czy jest liczbą
      list.append(num)
    except KeyboardInterrupt:
      print("Przerwano czytanie programu")
      return
    except ValueError:
      print(f"'{num_string}' - nie jest liczbą >:(")
    except Exception:
      raise
      
  return list
    

inputs = getList()
notNegative = [num for num in inputs if num >= 0]
averageNotNegative = sum(notNegative) / len(notNegative) if notNegative else "Nie istnieje"
inputs.sort()
smallest, greatest = inputs[0], inputs.pop()

print(f"Najmniejsza wartość: {smallest}\n" +
      f"Największa wartosć: {greatest}\n" +
      f"Średnia liczb nieujemnych: {averageNotNegative}")
