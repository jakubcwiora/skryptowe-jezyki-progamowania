with open("inwokacja.txt", "r", encoding="utf-8") as file:
  content = file.read()

new_lines = content.count("\n")
spaces = content.count(" ")
tabs = content.count("\t")

print(f"Liczba nowych linii: {new_lines}")
print(f"Liczba spacji: {spaces}")
print(f"Liczba tabulacji: {tabs}")
