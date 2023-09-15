from src.item import Item

item1 = Item('Smartphone', 1000, 5)
item2 = Item('Notebook', 2000.0, 10)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 5000
    assert item2.calculate_total_price() == 20000.0


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 500.0
    assert item2.price == 1000.0


def test_initiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5