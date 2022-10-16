poem = '''Программировать весело.\
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!'''

f = open('poem.txt', 'w') # Открываем для записи
f.write(poem) # записываем текст в файл
f.close() #закрываем файл

f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
        break
    else:
        print(line, end='')
f.close()
