import cmath

def solveQuadratic(a: float, b: float, c: float):
  if a == 0: # Sprawdzamy czy jest kwadratowe
    if b == 0: # Sprawdzamy czy jest liniowe
      return None
    return [-c / b]
  
  Delta = b * b - 4 * a * c 

  sqrtDelta = cmath.sqrt(Delta) # Używam cmath dal pierwiastków zespolonych
  return ((-b - sqrtDelta) / (2 * a), (-b + sqrtDelta) / (2 * a))

# proste pobieranie wejścia:
def prompt_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Podaj liczbę (np. 1, -2.5):")

# Wczytywanie zmiennych
a = prompt_float("Podaj a: ")
b = prompt_float("Podaj b: ")
c = prompt_float("Podaj c: ")

sols = solveQuadratic(a, b, c) # Rozwiązania
if sols is None:
    print("Brak rozwiązań lub nieskończenie wiele rozwiązań.")
else:
    print("Rozwiązania:", sols)
    