import csv


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
    def instantiate_from_csv(cls, file_name):
        Item.all = []
        with open(f'../{file_name}', 'r', newline='') as file:
            for row in csv.DictReader(file):
                Item(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string: str) -> int:
        return int(float(string))
