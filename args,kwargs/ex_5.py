# Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".


def print_table(**kwargs):
    if not kwargs:
        print("No data given.")
        return

    print(f"|{'Key':<15} | {'Value':<15}|")
    print("-" * 35)

    for key, value in kwargs.items():
        print(f"|{key:<15} | {value:<15}|")

print_table(name="Bob", age=30, city="Amsterdam")