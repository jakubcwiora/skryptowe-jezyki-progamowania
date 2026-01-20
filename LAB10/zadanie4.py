import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
  # Dane na osi X
  x = np.arange(0, 10)  # 0,1,2,...,9

  # Trzy serie losowych liczb całkowitych
  np.random.seed(42)  # dla powtarzalności wyników
  y1 = np.random.randint(-10, 21, size=10)  # zielone diamenty
  y2 = np.random.randint(-15, 26, size=10)  # żółte gwiazdki
  y3 = np.random.randint(-5, 16, size=10)  # fioletowe pięciokąty

  plt.figure(figsize=(9, 5.5))

  # 1. Zielone diamenty + linia ciągła
  plt.plot(
    x,
    y1,
    color="green",
    marker="D",  # diament
    linestyle="solid",
    linewidth=1.8,
    markersize=9,
    label="zielone diamenty",
  )

  # 2. Żółte gwiazdki + linia kropkowano-kreskowana
  plt.plot(
    x,
    y2,
    color="gold",
    marker="*",  # gwiazdka
    linestyle="-.",  # dash-dot
    linewidth=1.6,
    markersize=11,
    label="żółte gwiazdki",
  )

  # 3. Fioletowe pięciokąty + linia kreskowana
  plt.plot(
    x,
    y3,
    color="purple",
    marker="p",  # pentagon
    linestyle="--",  # dashed
    linewidth=1.7,
    markersize=10,
    label="fioletowe pięciokąty",
  )

  plt.xticks(x)
  plt.grid(True, linestyle=":", alpha=0.7)
  plt.title("Trzy serie losowych liczb całkowitych", fontsize=13, pad=12)
  plt.xlabel("kolejne liczby 0–9", fontsize=11)
  plt.ylabel("losowe liczby całkowite", fontsize=11)
  plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3)

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  main()
