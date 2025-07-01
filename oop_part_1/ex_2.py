# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от
# ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.


class TriangleChecker:
    def __init__(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in [a, b, c]):
            self.message = "Нужно вводить только числа!"
        elif not all(x >= 0 for x in [a, b, c]):
            self.message = "С отрицательными числами ничего не выйдет!"
        else:
            self.a = a
            self.b = b
            self.c = c
            self.message = None

    def is_triangle(self):
        if self.message:
            return self.message

        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


test_1 = TriangleChecker(3, 4, 5)
print(test_1.is_triangle())

test_2 = TriangleChecker(1, 2, 3)
print(test_2.is_triangle())

test_3 = TriangleChecker(-1, 2, 3)
print(test_3.is_triangle())

test_4 = TriangleChecker("a", 2, 3)
print(test_4.is_triangle())

test_5 = TriangleChecker(0, 2, 3)
print(test_5.is_triangle())
