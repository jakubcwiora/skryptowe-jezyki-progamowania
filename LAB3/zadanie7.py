def main() -> None:  
  tuple = ("apple", "banana", "cherry") 
  tuple_b = ("orange",) 
  tuple += tuple_b #dodawanie krotek 
  tuple += tuple_b #dodawanie krotek 
  multi_tuple = tuple * 2 #mnożenie krotek 
  print("Długość krotki: ", len(tuple)) #długość krotki - liczba elementów 
  for x in tuple: #wypisanie wszystkich elementów krotki 
    print(x)
  print("Długość po pomnożeniu przez 2: ", len(multi_tuple))
  for x in multi_tuple: #wypisanie wszystkich elementów krotki 
    print(x)
  
# a) Dodawanie krotek dopisuje element do końca krotki
# b) Dodanie dwa raxy tego samego elementu dodaje go dwa ray
# c) Mnożenie ktorek przez 'n' dodaje taką samą krotkę 'n' razy
# d) Przecinek tworzy krotke, bez niego wartość jest interpretowana jako string
# e) Krotki można tylko przepisać do nowego miejsca w pamięci przy użyciu 
# sorted()
    
if __name__ == "__main__":
  main()