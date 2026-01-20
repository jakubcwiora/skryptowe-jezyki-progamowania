import numpy as np
import matplotlib.pyplot as plt

dane = np.random.randint(0, 10, 100)

plt.figure(figsize=(10, 4.8))

plt.subplot(121)
plt.bar(*np.unique(dane, return_counts=True), color="teal", edgecolor="darkslategray")
plt.xticks(range(10))
plt.title("Wykres słupkowy")

plt.subplot(122)
plt.hist(dane, bins=range(11), color="orchid", edgecolor="purple", rwidth=0.92)
plt.xticks(range(10))
plt.title("Histogram")

plt.suptitle("100 losowych cyfr 0–9", fontsize=13)
plt.tight_layout()
plt.show()
