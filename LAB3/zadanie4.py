import random

def unevenNumbers():
  list = []
  for i in range(10):
    list.append(random.randint(0,1000))
  uneven = [num for num in list if num % 2 != 0]
  print(f"Lista: {list}\n" +
        f"Wartości nieparzyste: {uneven}")
  uneven.sort()
  print(f"Najmniejszy element nieparzysty: {uneven[0]}")
  
unevenNumbers()