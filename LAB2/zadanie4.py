import math # Wczytujemy 'math' 

def circumference(radius: float): # Obliczamy obwód
  return radius * 2 * math.pi

def area(radius: float):
  return math.pi * radius ** 2

def getData():
  while True:
    try:
      s = input("Podaj promień: ") # Wczytujemy wartość
      radius = float(s) # Rzutujemy na float
      print(f"Obwód wynosi: {circumference(radius)}")
      print(f"Pole wynosi: {area(radius)}") # Obliczamy
      break
    except ValueError: # Jeśli podano złą wartość (np. literę)
      print("Podaj liczbę!")
    except (KeyboardInterrupt): # Jeśli przerwano działanie (Ctrl + C)
      print("\nPrzerwano działanie.")
      break

getData()