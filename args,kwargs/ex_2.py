# Напишите функцию sum_of_squares, которая принимает произвольное
# количество позиционных аргументов, которые должны быть числами, и
# возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0.


def sum_of_squares(*args):
    if not args:
        return 0
    return sum(x ** 2 for x in args)

print(sum_of_squares(1,2,3,4,5,6))
print(sum_of_squares())