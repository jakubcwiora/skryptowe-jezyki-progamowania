import re

with open("inwokacja.txt", "r", encoding="utf-8") as file:
  content = file.read()

# Zamieniamy pojedyncze kropki na wielokropek, ale nie zmieniamy istniejących wielokropków
# Używamy regex, aby znaleźć kropki, które nie są częścią wielokropka
new_content = re.sub(r"\.(?=[^\\.]{2})", "...", content)

print(new_content)
