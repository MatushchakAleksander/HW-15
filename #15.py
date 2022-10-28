"""
Необходимо создать класс Human с атрибутами:

name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__

Так-же нужно написать методы:

get_info() - который возвращает словарь в котором находится информация о человеке
call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info
"""


class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        print(f"name:{self.name}\nsurname:{self.surname}\nage:{self.age}\nphone:{self.phone}\naddress:{self.address}")
        print()

    def call(self, phone_number):
        print(f"{self.phone} вызывает абонента {phone_number}")
        print()


p1 = Human("Petr", "Petrov", 25, "+3_050_123_45_62", "Ukraine, Odessa, Kanatnaya street, 15")
p2 = Human("Ivan", "Ivanov", 30, "+3_066_456_78_45", "Ukraine, Lviv, Chekhov street ,24")
p3 = Human("Oleg", "Somov", 35, "+3_099_437_88_90", "Ukraine, Dnepr, Hurtov  street, 56")

# Тесты
p1.get_info()
p2.get_info()
p3.get_info()

# p1.call(p2.phone)
