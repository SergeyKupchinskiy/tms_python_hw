# Напишите функцию calculate, которая принимает произвольное количество
# позиционных аргументов, которые должны быть числами, и один
# именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/".
# Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи.
# Если функции не передано ни одного позиционного аргумента, она должна
# вернуть 0.
# Если аргумент operation не указан, то по умолчанию используется "+".
# Пример вызова: calculate(1, 2, 3, operation="*")


def calculate(*args, operation="+"):
    if not args:
        return 0

    if operation not in {"+", "-", "*", "/"}:
        return ValueError("this operation is not available")

    result = args[0]

    for num in args[1:]:
        if operation == "+":
                result += num
        elif operation == "-":
                result -= num
        elif operation == "*":
                result *= num
        elif operation == "/":
            if num == 0:
                raise ZeroDivisionError("you can't divide by zero")
            result /= num

    return result


print(calculate(1, 2, 3, 4,operation="+"))
print(calculate(1, 2, 3, 4,operation="*"))
print(calculate(1, 2,operation="/"))
print(calculate(1, 2, 3, 4,operation="**"))
print(calculate(1, 2, 3, 4,operation="-"))
print(calculate(operation="+"))
print(calculate())
print(calculate(1, 0,operation="/"))