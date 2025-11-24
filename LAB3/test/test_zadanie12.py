import pytest
from LAB3.zadanie11 import average, add_student, create_gradebook

# --- average tests ---

def test_average_normal():
    assert average([4, 5, 3]) == pytest.approx(4.0)

def test_average_empty_returns_none():
    assert average([]) is None

def test_average_with_floats():
    assert average([4.5, 3.0, 2.5]) == pytest.approx((4.5+3.0+2.5)/3)

# --- add_student tests ---

def test_add_new_student():
    gb = {}
    add_student(gb, "2021999", "Ewa", "Malinowska", [5,4])
    assert "2021999" in gb
    s = gb["2021999"]
    assert s["imię"] == "Ewa"
    assert s["nazwisko"] == "Malinowska"
    assert s["oceny"] == [5,4]

def test_add_overwrites_existing():
    gb = create_gradebook()
    add_student(gb, "2021001", "Piotr", "Nowy", [2])
    s = gb["2021001"]
    assert s["imię"] == "Piotr"
    assert s["nazwisko"] == "Nowy"
    assert s["oceny"] == [2]

def test_add_default_oceny_empty_list():
    gb = {}
    add_student(gb, "2021888", "Klaudia", "B", None)
    assert gb["2021888"]["oceny"] == []