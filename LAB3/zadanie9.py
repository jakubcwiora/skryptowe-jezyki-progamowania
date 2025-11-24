from typing import Set

#def test_operations_on_sets(set_a, set_b) -> None:
def test_operations_on_sets() -> None:
  set_a: Set[int] = {1, 2, 3, 4, 5, 6}
  set_b: Set[int] = {4, 5, 6, 7, 8, 9}

  print(set_a.isdisjoint(set_b))
  print(set_a.issubset(set_b))
  print(set_a.issuperset(set_b))
  print(set_a.union(set_b))
  print(set_a.difference(set_b))
  print(set_a.intersection(set_b))

def main() -> None:
  test_operations_on_sets()

if __name__ == '__main__':
  main()