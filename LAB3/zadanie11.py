from typing import Dict, List, Optional

Student = Dict[str, object]
Gradebook = Dict[str, Student]


def create_gradebook() -> Gradebook:
  
  # Tworzy przykładowy arkusz ocen.
  # Kluczami są numery indeksów (str), wartościami słowniki z kluczami:
  # "imię", "nazwisko", "oceny" (lista ocen).
  
  return {
    "2021001": {"imię": "Jan", "nazwisko": "Kowalski", "oceny": [4, 5, 3, 4]},
    "2021002": {"imię": "Anna", "nazwisko": "Nowak", "oceny": [5, 5, 4]},
    "2021003": {"imię": "Piotr", "nazwisko": "Wiśniewski", "oceny": []}, 
  }


def add_student(gradebook: Gradebook, index: str, imie: str,
                 nazwisko: str, oceny: Optional[List[int]] = None) -> None:
  gradebook[index] = {"imię": imie, "nazwisko": nazwisko, "oceny": oceny or []}


def average(grades: List[float]) -> Optional[float]:
  # Zwraca średnią listy ocen lub None, gdy lista jest pusta.
  if not grades:
    return None
  return sum(grades) / len(grades)


def print_gradebook(gradebook: Gradebook) -> None:
  
  # Wypisuje wszystkich studentów: imię, nazwisko, numer indeksu oraz średnią z ocen.
  # Jeśli student nie ma ocen, wypisze 'brak ocen'.
  
  for index, info in gradebook.items():
    imie = info.get("imię", "?")
    nazwisko = info.get("nazwisko", "?")
    oceny = info.get("oceny", [])
    avg = average(oceny)
    avg_str = f"{avg:.2f}" if avg is not None else "brak ocen"
    print(f"{imie} {nazwisko} ({index}) - średnia: {avg_str}")


if __name__ == "__main__":
  # Przykładowe użycie
  arkusz = create_gradebook()
  add_student(arkusz, "2021004", "Maria", "Zielińska", [3, 4, 4, 5])
  print_gradebook(arkusz)