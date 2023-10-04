import csv
import os
from src.Exceptions import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Both objects must be instances of Items or it`s subclasses")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value
            
    @classmethod
    def instantiate_from_csv(cls, file_name=(os.path.join('../', 'src', 'items.csv'))):
        Item.all = []
        if not os.path.exists(file_name):
            raise FileNotFoundError('Отсутствует файл item.csv')
        with open(f'{file_name}', 'r', newline='') as file:
            for row in csv.DictReader(file):
                if not {'name', 'price', 'quantity'}.issubset(set(row.keys())):
                    raise InstantiateCSVError
                Item(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string: str) -> int:
        return int(float(string))
