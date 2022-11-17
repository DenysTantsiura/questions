OOPS = 'Index not found!'
print('a')
BADLY_MESSAGE = {
    'name': 'Name incorrect',
    'bloke': 'Bloke incorrect',
}


class Field:  # superclass for all base fields
    """A base class with a simple field."""

    def __init__(self):
        self._value = None
        self.__bloke = None

    def __str__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._value = new_value
    
    @property
    def bloke(self):
        return self.__bloke

    @bloke.setter
    def bloke(self, new_bloke: str):
        self.__bloke = new_bloke


class Name(Field):
    """Class of username."""
    @Field.value.setter
    def value(self, new_value: str):

        if new_value[0].isalpha():  # not in 'ьъыЫЬЪ\'"[]_0123456789!@$%^&*()-+?<>~`|\\/'
            self._value = new_value

        else:
            print(BADLY_MESSAGE.get('name', OOPS))

    @Field.bloke.setter
    def bloke(self, new_bloke: str):

        if new_bloke[0].isalpha():  # not in 'ьъыЫЬЪ\'"[]_0123456789!@$%^&*()-+?<>~`|\\/'
            self._Field__bloke = new_bloke

        else:
            print(BADLY_MESSAGE.get('bloke', OOPS))


a = Name()
print(a)
a.value = 'Alpha'
print(a)
print(a.value)
print(a.bloke)
a.bloke = 'Centauri'
print(a.bloke)
