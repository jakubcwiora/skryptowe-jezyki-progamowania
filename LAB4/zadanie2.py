class Vehicle:
  def get_sound(self) -> None:
    print("vehicle's brum brum")


class Car(Vehicle):
  def __init__(self, owner: str, table: str):
    self.owner = owner
    self.table = table

  def get_sound(self) -> None:
    print("car's brum brum")

  def get_owner(self) -> str:
    return self.owner


v = Vehicle()
c = Car("Alice", "XYZ-123")

v.get_sound()  # wywoła Vehicle.get_sound
c.get_sound()  # wywoła Car.get_sound (nadpisanie/metoda override)

# Wywołanie get_owner dla obu obiektów:
print("car owner:", c.get_owner())
# print("vehicle owner:", v.get_owner())  # AttributeError: 'Vehicle' object has no attribute 'get_owner'
