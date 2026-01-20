import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
  x = np.linspace(-np.pi, np.pi, 100)  # przedział [-pi,pi]
  f = np.sin(x)  # sin(x) dla argumentów z tablicy x
  g = 2 * np.cos(x)
  plt.plot(x, f)  # wykres, wymagane 2 tablice o tych samych wymiarach
  plt.plot(x, g)
  plt.title("Wykresy funkcji trygonometrycznych")
  plt.xlabel("Oś x")
  plt.ylabel("Oś y")
  plt.legend(["sin(x)", "2cos(x)"])
  plt.show()  # wyświetlenie wykresu na ekranie


if __name__ == "__main__":
  main()
