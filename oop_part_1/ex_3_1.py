# Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы: - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),  - get_kg() - для вывода текущего значения кг.
# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.


class KgToPounds:
    def __init__(self, kg):
        self.__kg = None
        self.set_kg(kg)

    def to_pounds(self):
        return self.__kg * 2.20462

    def set_kg(self, value):
        if isinstance(value, (int, float)):
            self.__kg = value
        else:
            print("Значение должно быть числом!")

    def get_kg(self):
        return self.__kg


converter = KgToPounds(10)
print(f"{converter.get_kg()} кг = {converter.to_pounds():.2f} фунтов")

converter.set_kg(5.5)
print(f"{converter.get_kg()} кг = {converter.to_pounds():.2f} фунтов")

converter.set_kg("abc")
print(f"{converter.get_kg()} кг = {converter.to_pounds():.2f} фунтов")