# Miejsce na shebang

# Miejsce na importy

def greetings(): # Funkcja wypisująca powitanie
  print('Hello World')
  
def main() -> None: # Deklaracja main-a który wywołuje greetings()
  greetings()

if __name__ == '__main__': # Wywołanie main-a
  main()
