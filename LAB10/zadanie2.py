import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
  labels = "Frogs", "Cats", "Dogs"
  sizes = [25, 30, 45]
  explode = (0, 0.1, 0)
  fig1, ax1 = plt.subplots()
  ax1.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
  )
  plt.show()


if __name__ == "__main__":
  main()
