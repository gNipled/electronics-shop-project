import pytest

from src.keyboard import Keyboard

item1 = Keyboard('Smartphone', 1000, 5)


def test___str__():
    assert str(item1) == 'Smartphone'


def test___repr__():
    assert repr(item1) == "Keyboard('Smartphone', 1000, 5, EN)"


def test_change_lang():
    assert item1.language == 'EN'
    item1.change_lang()
    assert item1.language == 'RU'
