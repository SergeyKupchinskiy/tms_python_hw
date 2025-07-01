# Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString.


class RealString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self) == len(other)
        elif isinstance(other, str):
            return self.string == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self) < len(other)
        elif isinstance(other, str):
            return self.string < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, RealString):
            return len(self) <= len(other)
        elif isinstance(other, str):
            return self.string <= other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RealString):
            return len(self) > len(other)
        elif isinstance(other, str):
            return self.string > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, RealString):
            return len(self) >= len(other)
        elif isinstance(other, str):
            return self.string >= other
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, RealString):
            return len(self) != len(other)
        elif isinstance(other, str):
            return self.string != other
        else:
            return NotImplemented

a = RealString("abc")
b = RealString("defg")
s = "abc"

print(a.__len__() == 3)

print(a.__eq__(b) == False)

print(a.__eq__(s) == True)

print(a.__lt__(b) == True)

print(b.__gt__(s) == True)

print(a.__ne__(b) == True)