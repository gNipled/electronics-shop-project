import pytest

from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test___str__():
    assert str(phone1) == 'iPhone 14'


def test___repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test___init__():
    with pytest.raises(ValueError) as excinfo:
        Phone("iPhone 14", 120_000, 5, 3.8)
    assert str(excinfo.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
    with pytest.raises(ValueError) as excinfo:
        Phone("iPhone 14", 120_000, 5, -4)
    assert str(excinfo.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
