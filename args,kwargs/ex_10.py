# Напишите функцию create_student, которая создает словарь студента
# для учебного заведения, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, фамилия, отчество и группа.
# Также дополнительными параметрами могут быть: дата поступления в виде
# строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес.
# Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть
# в словаре.


def create_student(name, surname, patronymic, group, **kwargs):

    student = {
        'name': name,
        'surname': surname,
        'patronymic': patronymic,
        'group': group
    }
    for key, value in kwargs.items():
        if value is not None:
            student[key] = value
    return student

student_1 = create_student("Nicolas","Cage","Ivanovich","HL-101", date_of_admission="19.10.2023", average_grade=4.5, semester=2, phone_number="+88-991-123-45-67")
student_2 = create_student("John", 'Cena',"Djeimsovich", "WR-404")
print(student_1)
print(student_2)