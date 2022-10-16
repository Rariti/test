try:
    text = input('Введите что нибудь --->')
except EOFError:
    print('Ну зачем вы сделали EOFError')
except KeyboardInterrupt:
    print('Нузачем мне KeyboardInterrupt')
else:
    print('Все впорядке {0}'.format(text))