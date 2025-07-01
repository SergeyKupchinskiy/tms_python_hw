# Напишите класс Person, который имеет атрибуты name (имя), age (возраст)
# и gender (пол). Класс должен иметь следующие методы:
# • Конструктор, который принимает три параметра: name, age и gender, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Person в формате “Имя: name, Возраст: age, Пол: gender”.
# • Метод get_name, который возвращает значение атрибута name.
# • Метод set_name, который принимает один параметр: new_name, и
# устанавливает значение атрибута name равным new_name. Этот метод
# должен быть декорирован как property.
# • Метод is_adult, который возвращает True, если возраст объекта больше
# или равен 18, и False в противном случае. Этот метод должен быть
# декорирован как staticmethod.
# • Метод create_from_string, который принимает один параметр: s, и
# создает и возвращает объект класса Person на основе строки s. Строка s
# должна иметь формат “name-age-gender”, где name - имя, age - возраст и
# gender - пол. Этот метод должен быть декорирован как classmethod.


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}, пол: {self.gender}'

    def get_name(self):
        return self._name

    @property
    def set_name(self):
        return self.get_name

    @set_name.setter
    def set_name(self, new_name):
        self._name = new_name

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def create_from_string(cls, s):
        parts = s.split('-')
        if len(parts) != 3:
            raise ValueError("Строка должна иметь формат 'name-age-gender'")
        name, age_str, gender = parts
        try:
            age = int(age_str)
        except ValueError:
            raise ValueError("Возраст должен быть числом")
        return cls(name, age, gender)


p = Person("Иван", 20, "муж")
print(p.name)
print(p.age)
print(p.gender)

p.set_name = "Пётр"
print(p.get_name())

print(Person.is_adult(p.age) is True)

p_2 = Person.create_from_string("Мария-30-жен")
print(p_2.name)
print(p_2.age)
print(p_2.gender)