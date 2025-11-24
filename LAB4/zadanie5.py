class Item:
  def get_sound(self) -> None:
    print("item's sound")


class Element:
  def get_sound(self) -> None:
    print("element's sound")


class Thing(Element, Item):
  def say_hello(self) -> None:
    print("hello!")


item = Item()
element = Element()
thing = Thing()

print("Item sound:")
item.get_sound()

print("Element sound:")
element.get_sound()

print("Thing sound:")
thing.get_sound()


# Change order
class Thing(Item, Element):
  def say_hello(self) -> None:
    print("hello!")


thing2 = Thing()
print("Thing sound after changing order:")
thing2.get_sound()
