import re

# Zadanie 1: Testowanie kwantyfikatorów zachłannych i leniwych

# Przykładowy tekst do testowania
text = "aaaa"

# Kwantyfikatory zachłanne
print("Zachłanne kwantyfikatory:")
print("a+:", re.findall("a+", text))  # Dopasowuje wszystkie 'a' naraz
print(
  "a*:", re.findall("a*", text)
)  # Dopasowuje wszystkie 'a' naraz (w tym pusty przed pierwszym)
print("a?:", re.findall("a?", text))  # Dopasowuje każdą literę osobno (a lub nic)

# Kwantyfikatory leniwe
print("\nLeniwe kwantyfikatory:")
print("a+?:", re.findall("a+?", text))  # Dopasowuje jedną 'a' za każdym razem
print("a*?:", re.findall("a*?", text))  # Dopasowuje pusty ciąg przed każdą 'a'
print("a??:", re.findall("a??", text))  # Dopasowuje pusty ciąg przed każdą 'a'

# Opis wyników w sprawozdaniu:
# - a+ (zachłanny): ['aaaa'] - jedno długie dopasowanie
# - a+? (leniwy): ['a', 'a', 'a', 'a'] - cztery krótkie dopasowania
# - a* (zachłanny): ['', 'aaaa', ''] - pusty na początku, wszystkie 'a', pusty na końcu
# - a*? (leniwy): ['', '', '', '', ''] - pięć pustych dopasowań
# - a? (zachłanny): ['a', '', 'a', '', 'a', '', 'a', ''] - alternuje a i pusty
# - a?? (leniwy): ['', 'a', '', 'a', '', 'a', '', 'a', ''] - pusty przed każdą a
