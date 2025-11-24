from typing import Dict

def main() -> None:
  car_dict: Dict = { 
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964, 
    "new": False 
  }
  car_dict["milage"] = 2 * 10 ** 6
  car_dict["year"] = 1975
  car_dict[1] = "test"
  print("Przed pop/popit: ", car_dict)
  car_dict.pop("year")
  car_dict.popitem() # usuwa ostatnio dodany element
  print("Po pop/popit: ", car_dict)

if __name__ == "__main__":
  main()

