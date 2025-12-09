import re

# Zadanie 2: Użycie lookaround na pliku "Inwokacji"
# Zakładam przykładową zawartość pliku "Inwokacji" (fragment wiersza Mickiewicza dla demonstracji)
# W rzeczywistości wczytaj plik: with open('Inwokacji.txt', 'r', encoding='utf-8') as f: text = f.read()

text = """
Litwo! Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.
Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
"""

# 1. Wypisać słowa po których występuje „!”
words_after_exclamation = re.findall(r"\b\w+\b(?=\s*!)", text)
print("Słowa po których występuje „!”:", words_after_exclamation)

# 2. Wypisać słowa z polskimi znakami (ż, ą, ę, ś, ć, ń, ó, ł)
polish_words = re.findall(r"\b\w*[ąćęłńóśźż]+\w*\b", text, re.IGNORECASE)
print("Słowa z polskimi znakami:", polish_words)

# 3. Zliczyć wystąpienia słowa cię/ci
count_cie_ci = len(re.findall(r"\b(cię|ci)\b", text, re.IGNORECASE))
print("Liczba wystąpień słowa cię/ci:", count_cie_ci)
