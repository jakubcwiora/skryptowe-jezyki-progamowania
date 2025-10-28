from typing import Optional, List

def get_list() -> Optional[List[float]]:
  nums: List[float] = []
  while len(nums) < 10:
    # najpierw tylko wczytanie — obsługujemy przerwanie/EOF
    try:
      num_string = input("Podaj liczbe: ")
    except (KeyboardInterrupt, EOFError):
      print("Przerwano czytanie programu")
      return None
    # następnie obsługujemy błąd wczytanej wartości
    try:
      num = float(num_string)
    except ValueError:
      print(f"'{num_string}' - nie jest liczbą >:(")
      continue
    nums.append(num)
  return nums
    
def main() -> None:
  inputs = get_list()
  if inputs is None:
    print("Nie wykonuje programu")
    return

  notNegative = [num for num in inputs if num >= 0]
  averageNotNegative = sum(notNegative) / len(notNegative) if notNegative else "Nie istnieje"
  inputs.sort()
  smallest, greatest = inputs[0], inputs[-1]
  print(f"Najmniejsza wartość: {smallest}\n" +
        f"Największa wartosć: {greatest}\n" +
        f"Średnia liczb nieujemnych: {averageNotNegative}")

if __name__ == "__main__":
  main()