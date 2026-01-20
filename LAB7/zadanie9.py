import os
import re

# Wyrażenie regularne dla plików .txt
pattern = re.compile(r".*\.txt$")

directory = input("Podaj ścieżkę do katalogu: ")

if os.path.isdir(directory):
  for file in os.listdir(directory):
    if pattern.match(file):
      print(file)
else:
  print("Niepoprawna ścieżka katalogu")
