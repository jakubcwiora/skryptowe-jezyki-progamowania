import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
  fig, ax = plt.subplots()
  fruits = ["apple", "blueberry", "cherry", "orange", "grape"]
  counts = [40, 100, 30, 55, 70]
  bar_labels = ["apple", "blueberry", "cherry", "orange", "grape"]
  bar_colors = ["red", "blue", "red", "orange", "purple"]
  ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
  ax.set_ylabel("ilość owoców")
  ax.set_title("Owoce kture zjadłem :)")
  ax.legend(title="Legenda")
  plt.show()


if __name__ == "__main__":
  main()
