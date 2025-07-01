# Создайте класс Soda (для определения типа газированной воды), принимающий
# 1 аргумент при инициализации (отвечающий за добавку к выбираемому
# лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на
# печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе
# отобразится следующая фраза: «Обычная газировка».


class Soda:
    def __init__(self, addiction=None):
        self.addiction = addiction

    def show_my_drink(self):
        if self.addiction:
            print(f"Газировка {self.addiction}")
        else:
            print("Обычная газировка")


drink1 = Soda()
drink1.show_my_drink()

drink2 = Soda("Фанта")
drink2.show_my_drink()