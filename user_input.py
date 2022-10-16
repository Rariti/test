def revers(text):
    return text[::-1]
def is_polindrom(text):
    return text == revers(text)
a = True

while a > 0:
    somithing = input('Введите текст: ')
    b = somithing.lower()
    d = b.replace(' ', '')
    if is_polindrom(d):
        print('Да, это полиндром')
    else:
        print('Нет, это не полиндром')