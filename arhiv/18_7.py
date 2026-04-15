import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
predmets = ['Русский язык','Математика','Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for predmet in predmets:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][predmet] = marks
#Выводим на экран журнал успеваемости
for student in students:
    print(f'''{student}
    {students_marks[student]}''')
print(''' 
Список команд:
1. Добавить оценку ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить данные по оценкам
5. Редактировать данные по оценкам
6. Удалить данные по предметам
7. Редактировать название предмета
8. Изменить имя ученика
9. Удалить ученика
10. Все оценки для выбранного ученика
11. Средний бал по каждому предмету для выбранного ученика
12. Выход из программы
''')
while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1.  Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        predmet = input('Введите название предмета: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and predmet in students_marks[student].keys():
            students_marks[student][predmet].append(mark)
            print(f'Для студента {student} добавлена оценка по предмету {predmet} - {mark}')
            print(students_marks)
        else:
            print('Неправильно введено имя ученика или предмет.')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for predmet in predmets:
                predmet_sum = sum(students_marks[student][predmet])
                predmet_count = len(students_marks[student][predmet])
                print(f'\t{predmet} - {predmet_sum // predmet_count}')
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for predmet in predmets:
                print(f'\t{predmet} {students_marks[student][predmet]}')
    elif command == 4:
        print('4. Удалить данные по оценкам')
        student = input('Введите имя ученика: ')
        if student in students:
            predmet = input('Введите название предмета: ')
            if predmet in predmets:
                mark_del = int(input('Введите оценку, которую хотите удалить: '))
                if mark_del in students_marks[student][predmet]:
                    students_marks[student][predmet].remove(mark_del)
                else:
                    print('Такой оценки нет.')
            else:
                print('Такого предмета нет.')
        else:
            print('Такого ученика нет.')
    elif command == 5:
        print('5. Редактировать данные по оценкам')
        student = input('Введите имя ученика: ')
        if student in students:
            predmet = input('Введите название предмета: ')
            if predmet in predmets:
                mark_index = int(input('Введите порядковый номер оценки, которую хотите изменить: '))
                if mark_index <= len(students_marks[student][predmet]):
                    mark_new = int(input('Введите новое значение оценки: '))
                    students_marks[student][predmet][mark_index - 1] = mark_new
                else:
                    print('Вы ввели цифру, большую, чем кол-во оценок.')
            else:
                print('Такого предмета нет.')
        else:
            print('Такого ученика нет.')
    elif command == 6:
        print('6. Удалить данные по предметам')
        predmet_del = input('Введите название предмета, который надо удалить: ')
        if predmet_del in predmets:
            predmets.remove(predmet_del)
            print(f'Остались предметы: {predmets}')
# Удаляем записи по удаленному предмету из базы оценок
            for student in students:
                del students_marks[student][predmet_del]
        else:
            print('Нет такого предмта.')
    elif command == 7:
        print('7. Редактировать название предмета')
        predmet_edit = input('Введите название изменяемого предмета: ')
        if predmet_edit in predmets:
            predmet_new = input('Введите новое название предмета: ')
            predmets[predmets.index(predmet_edit)] = predmet_new
            print(f'Список новых предметов: {predmets}')
# Обновляем данные по новому названию предмета в базе оценок
            for student in students:
                students_marks[student][predmet_new] = students_marks[student].pop(predmet_edit)
        else:
            print('Нет такого предмета.')
    elif command == 8:
        print('8. Изменить имя ученика')
# Смена имени ученика
        student_edit = input('Введите имя ученика, которое надо изменить: ')
        if student_edit in students:
            student_new = input('Введите новое имя ученика: ')
            students[students.index(student_edit)] = student_new
            print(f'Имя ученика {student_edit} изменено на {student_new}.')
# Обновляем данные по новому имени в базе
            students_marks[student_new] = students_marks.pop(student_edit)
        else:
            print('Нет такого ученика.')
    elif command == 9:
        print('9. Удалить ученика')
        student_del = input('Введите имя удаляемого ученика: ')
        if student_del in students:
            students.remove(student_del)
# Удаляем в журнале оценок запись для удаленного ученика
            students_marks.pop(student_del)
        else:
            print('Нет такого ученика.')
    elif command == 10:
        print('10. Все оценки для выбранного ученика')
        student_select = input('Введите имя ученика: ')
        if student_select in students:
            print(f'Оценки ученика {student_select}:')
            for predmet in predmets:
                print(f'\t {predmet}  {students_marks[student_select][predmet]}')
        else:
            print('Нет такого ученика.')
    elif command == 11:
        print('11. Средний бал по каждому предмету для выбранного ученика')
        student_select = input('Введите имя ученика: ')
        if student_select in students:
            print(f'Средний бал ученика {student_select} по каждому предмету:')
            for predmet in predmets:
                predmet_sum = sum(students_marks[student_select][predmet])
                predmet_count = len(students_marks[student_select][predmet])
                print(f'\t{predmet} - {predmet_sum // predmet_count}')
        else:
            print('Нет такого ученика.')
    elif command == 12:
        print('12. Выход из программы')
        break

