# Globalna zmienna
a: int = 10

# Globalna stała 
A: int = 100

def printFromFunction():
    
    a = 5 # Nadpisujemy wartość
    print("Lokalne a:", a)       
    print("Globalne A:", A)       
    print("Typ lokalnego a:", type(a))      
    print("Typ globalnego A:", type(A))     


printFromFunction()

print("Globalne a poza funkcją:", a)
print("Globalne A poza funkcją:", A)
