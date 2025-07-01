# Напишите класс Rectangle, который имеет атрибуты: width (ширина) и
# height (высота). Класс должен иметь следующие методы:
# • Конструктор, который принимает два параметра: width и height, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Rectangle в формате “Прямоугольник с шириной width и высотой
# height”.
# • Метод get_area, который возвращает площадь прямоугольника.
# • Метод get_perimeter, который возвращает периметр прямоугольника.
# • Метод is_square, который возвращает True, если прямоугольник является
# квадратом, и False в противном случае. Этот метод должен быть
# декорирован как property.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Прямоугольник с шириной {self.width} и высотой {self.height})'

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        return self.width == self.height


rect = Rectangle(3, 4)

print(rect.width == 3)
print(rect.height == 4)

print(str(rect) == 'Прямоугольник с шириной 3 и высотой 4)')

print(rect.get_area() == 12)

print(rect.get_perimeter() == 14)

print(rect.is_square == False)

square = Rectangle(5, 5)
print(square.is_square == True)