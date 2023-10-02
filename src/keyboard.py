from src.item import Item


class MixinLanguage:
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(MixinLanguage, Item):
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

