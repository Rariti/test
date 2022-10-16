class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что нибудь --->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('Длина введеной строки {0} Ожидалось как минимум {1}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений')