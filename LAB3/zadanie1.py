def operationsOnList():
  list = []                                       # a)
  for i in range(5):  
    list.append(i)                                # b) 
  print("2 pierwsze i 2 ostatnie elementy: ",
        list[0], list[1], list[3], list[4])       # c)
  print(f'Długość listy = {len(list)}')           # d)
  print("Wartości na indeksach parzystych",
        list[::2])                                # e)
  list.append(255)                                # f)
  list.append("element")                          # g)
  # h)  list.sort() nie zadziała przez rożne typy zmiennych 
  list.remove("element")                          # i)
  list.sort()
  list.reverse()                                  # j)
  list.insert(2, 'wartosc')                       # k)
  list.count(13)                                  # l)
  
operationsOnList()