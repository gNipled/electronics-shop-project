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
