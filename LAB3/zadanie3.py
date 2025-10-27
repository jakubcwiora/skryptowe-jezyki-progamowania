import random

def generateLists():
  list1 = []
  list2 = []
  for i in range(random.randint(5,10)):
    list1.append(random.randint(0,10))
    list2.append(random.randint(0,10))
  unique = set([num for num in list1 if num not in list2 ])
  
  print(f"Pierwsza lista: {list1}\n" +
        f"Druga lista {list2}\n" +
        f"Wartości unikatowe pierwszej listy {unique}")
  
generateLists()