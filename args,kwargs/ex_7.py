# Напишите функцию print_triangle, которая принимает один именованный
# аргумент height, который должен быть положительным целым числом, и
# выводит равнобедренный треугольник из символов "*" с заданной высотой.
# Если аргумент height не указан, то по умолчанию используется число 5.
# Пример вызова: print_triangle(height=4)


def print_triangle(height=5):
    if height <= 0:
        print("height cannot be a negative number")
        return

    for i in range(height):

        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

print_triangle()
print_triangle(3)