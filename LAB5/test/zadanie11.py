from LAB5.zadanie2 import get_bit  # Assuming zadanie2.py is accessible


def test_get_bit_zero():
  assert get_bit(0, 0) == 0
  assert get_bit(0, 7) == 0


def test_get_bit_max():
  assert get_bit(255, 0) == 1
  assert get_bit(255, 7) == 1


def test_get_bit_middle():
  assert get_bit(12, 0) == 0  # 12 = 1100, bit 0 is 0
  assert get_bit(12, 2) == 1  # bit 2 is 1


def test_get_bit_wrong_input():
  assert get_bit("s", 32.1) is TypeError("Number must be an integer.")
  assert get_bit(4, "2.1") is TypeError("Bit index must be an integer.")


# Run tests (in terminal: pytest zadanie11.py)
# Results would show passed/failed for each test
