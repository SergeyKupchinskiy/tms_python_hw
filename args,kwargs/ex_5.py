# Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".


def print_table(**kwargs):
    if not kwargs:
        print("No data given.")
        return

    key_width = max(len("Key"), *(len(str(k)) for k in kwargs.keys()))
    value_width = max(len("Value"), *(len(str(v)) for v in kwargs.values()))

    print(f"| {'Key':<{key_width}} | {'Value':<{value_width}} |")
    print(f"| {'-' * key_width}-|-{'-' * value_width} |")

    for key, value in kwargs.items():
        print(f"| {str(key):<{key_width}} | {str(value):<{value_width}} |")

print_table(name="Bob", age=30, city="Amsterdam")