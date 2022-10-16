from abc import *

class SchoolMember(metaclass=ABCMeta):
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Создаём SchoolMember: {0}'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Вывести информацию.'''
        print('Имя: "{0}" Возраст: "{1}"'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Создаём Teacher: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: {0:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создаем Student: "{0}"'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Мистер Жвановский', 45, 35000)
s = Student('GuJobe', 25, 99)

#m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"
print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell()