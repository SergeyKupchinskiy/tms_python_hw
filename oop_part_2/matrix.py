class Matrix:
    def __init__(self, data):
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Матрица не должна быть пустой")
        row_length = len(data[0])
        if any(len(row) != row_length for row in data):
            raise ValueError("Строки должны быть одинаковой длинны")
        self.data = data
        self.rows = len(data)
        self.cols = row_length

    def __check_same_size(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Объект должен являться матрицей")
        if self.size() != other.size():
            raise ValueError("Матрицы должны быть одинакового размера")

    def __add__(self, other):
        self.__check_same_size(other)
        new_data = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(new_data)

    def __sub__(self, other):
        self.__check_same_size(other)
        new_data = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(new_data)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_data = [
                [self.data[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(new_data)
        else:
            raise TypeError("Можно умножать только на число")

    def transpose(self):
        new_data = [
            [self.data[i][j] for i in range(self.rows)]
            for j in range(self.cols)
        ]
        return Matrix(new_data)

    @classmethod
    def identity(cls, m, n):
        data = [
            [1 if i == j else 0 for j in range(n)]
            for i in range(m)
        ]
        return cls(data)

    @classmethod
    def zero(cls, m, n):
        data = [
            [0 for _ in range(n)]
            for _ in range(m)
        ]
        return cls(data)

    @classmethod
    def diagonal(cls, values):
        size = len(values)
        data = [
            [values[i] if i == j else 0 for j in range(size)]
            for i in range(size)
        ]
        return cls(data)

    def size(self):
        return (self.rows, self.cols)

    def count_elements(self):
        return self.rows * self.cols

    def sum_elements(self):
        return sum(sum(row) for row in self.data)

    def replace_negatives_with_zero(self):
        new_data = [
            [item if item >= 0 else 0 for item in row]
            for row in self.data
        ]
        return Matrix(new_data)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.size() != other.size():
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __str__(self):
        rows_str = ["\t".join(map(str, row)) for row in self.data]
        return "\n".join(rows_str)

m1 = Matrix([[-1, 3], [0, 1], [-2, 2]])
m2 = Matrix([[1, 2], [3, 4], [5, 6]])

print("Матрица m1:")
print(m1)
print("\nМатрица m2:")
print(m2)

print("\nСумма матриц m1 и m2:")
print(m1 + m2)

print("\nРазница матриц m2 и m1:")
print(m2 - m1)

print("\nУмножение матрицы m1 на 3:")
print(m1 * 3)

print("\nТранспонирование матрицы m1:")
print(m1.transpose())

print("\nЕдиничная матрица 3x3:")
print(Matrix.identity(3, 3))

print("\nНулевая матрица 2x4:")
print(Matrix.zero(2, 4))

print("\nДиагональная матрица из списка [1,2,3]:")
print(Matrix.diagonal([1, 2, 3]))

print("\nКортеж m1:", m1.size())
print("Общее количество элементов в матрице m1:", m1.count_elements())
print("Сумма всех чисел в матрице m1:", m1.sum_elements())

print("\nМатрица m1 где все отрицательные элементы заменены на 0:")
print(m1.replace_negatives_with_zero())

print("\nПроверка равенства матриц m1 и m1:", m1 == m1)
print("Проверка равенства матриц m1 и m2:", m1 == m2)