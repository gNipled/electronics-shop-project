import pytest

from src.item import Item

item1 = Item('Smartphone', 1000, 5)
item2 = Item('Notebook', 2000.0, 10)
item3 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 5000
    assert item2.calculate_total_price() == 20000.0


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 500.0
    assert item2.price == 1000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    item = Item.all[0]
    assert item.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test___str__():
    assert str(item3) == 'Смартфон'


def test___repr__():
    assert repr(item3) == "Item('Смартфон', 10000, 20)"


def test___add__():
    assert item1 + item2 == 15
    with pytest.raises(TypeError) as excinfo:
        item1 + 3
    assert str(excinfo.value) == 'Both objects must be instances of Items or it`s subclasses'
