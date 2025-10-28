from typing import Set, Optional

def test_set_operations() -> None:
  fruits: Set[str] = {"apple", "banana", "cherry", "orange", "kiwi"}
  print("Początkowy zbiór:", fruits)
  # a) remove vs discard
  # remove usuwa element, jeśli go nie ma -> KeyError
  try:
    fruits.remove("banana")
    print("Po remove('banana'):", fruits)
  except KeyError:
    print("remove('banana') - elementu nie ma w zbiorze (KeyError)")
  # discard robi to samo co remove, ale nie podnosi wyjątku gdy elementu brak
  fruits.discard("banana")  # nic się nie stanie (bez wyjątku)
  print("Po discard('banana') (bez wyjątku jeśli brak):", fruits)
  # b) pop - usuwa i zwraca 'jakikolwiek' element
  print("\nDemonstracja pop():")
  temp = set(fruits)  # robimy kopię, żeby nie modyfikować oryginału na stałe
  print("Kopia przed popami:", temp)
  popped_order = []
  while temp:
    popped = temp.pop()
    popped_order.append(popped)
    print("pop() ->", popped, "| pozostało:", temp)
  print("Kolejność usuwania przez pop w tej sesji:", popped_order)
  print("Uwaga: kolejność może wyglądać deterministycznie w jednej sesji," +
      "ale nie jest gwarantowana przez specyfikację Pythona i może się zmieniać między uruchomieniami/interpreterami.")
  # pop() na pustym zbiorze podniesie KeyError
  try:
    set().pop()
  except KeyError:
    print("pop() na pustym zbiorze -> KeyError")

if __name__ == "__main__":
  test_set_operations()
