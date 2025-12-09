with open("inwokacja.txt", "r", encoding="utf-8") as file:
  content = (
    file.read().strip()
  )  # Usuwamy białe znaki z lewej i prawej strony całego tekstu

lines = content.split("\n")  # Dzielimy na wiersze
total_lines = len(lines)
total_chars = 0
total_words = 0

print(f"Liczba wierszy: {total_lines}")

for i, line in enumerate(lines, 1):
  line = line.strip()  # Dodatkowe usunięcie białych znaków dla każdego wiersza
  chars = len(line)
  words = len(line.split()) if line else 0
  total_chars += chars
  total_words += words
  print(f"Wiersz {i}: {chars} znaków, {words} wyrazów")

print(f"Suma znaków w całym tekście: {total_chars}")
print(f"Suma wyrazów w całym tekście: {total_words}")
