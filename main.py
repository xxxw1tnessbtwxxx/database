import sqlite3

def create():

    with sqlite3.connect('examenation.db') as db:
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS lessons (
            subject TEXT,
            hours INTEGER,
            teacher TEXT,
            exam_view TEXT,
            time TEXT,
            audience INTEGER
            )""")

        db.commit()

        c.execute("""CREATE TABLE IF NOT EXISTS grades (
        subject TEXT,
        count_5 INTEGER,
        count_4 INTEGER,
        count_3 INTEGER,
        count_2 INTEGER
        )""")

        db.commit()

        c.execute("""CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        group_name TEXT,
        math INTEGER,
        programming INTEGER,
        discrete_math INTEGER,
        history INTEGER,
        english_lang INTEGER
        )""")

        db.commit()
    db.close()

create()

def update_counter(math: int, programming: int, discrete_math: int, history: int, english_lang: int):
    with sqlite3.connect('examenation.db') as db:
        c = db.cursor()

        if math == 5:
            c.execute("""UPDATE grades SET count_5 = count_5 + 1 WHERE subject = 'math'""")
            db.commit()

        elif math == 4:
            c.execute("""UPDATE grades SET count_4 = count_4 + 1 WHERE subject = 'math'""")
            db.commit()

        elif math == 3:
            c.execute("""UPDATE grades SET count_3 = count_3 + 1 WHERE subject = 'math'""")
            db.commit()

        elif math == 2:
            c.execute("""UPDATE grades SET count_2 = count_2 + 1 WHERE subject = 'math'""")
            db.commit()

        
        if programming == 5:
            c.execute("""UPDATE grades SET count_5 = count_5 + 1 WHERE subject = 'programming'""")

        elif programming == 4:
            c.execute("""UPDATE grades SET count_4 = count_4 + 1 WHERE subject = 'programming'""")

        elif programming == 3:
            c.execute("""UPDATE grades SET count_3 = count_3 + 1 WHERE subject = 'programming'""")

        elif programming == 2:
            c.execute("""UPDATE grades SET count_2 = count_2 + 1 WHERE subject = 'programming'""")

        if discrete_math == 5:
            c.execute("""UPDATE grades SET count_5 = count_5 + 1 WHERE subject = 'discrete_math'""")

        elif discrete_math == 4:
            c.execute("""UPDATE grades SET count_4 = count_4 + 1 WHERE subject = 'discrete_math'""")

        elif discrete_math == 3:
            c.execute("""UPDATE grades SET count_3 = count_3 + 1 WHERE subject = 'discrete_math'""")

        elif discrete_math == 2:
            c.execute("""UPDATE grades SET count_2 = count_2 + 1 WHERE subject = 'discrete_math'""")

        if history == 5:
            c.execute("""UPDATE grades SET count_5 = count_5 + 1 WHERE subject = 'history'""")

        elif history == 4:
            c.execute("""UPDATE grades SET count_4 = count_4 + 1 WHERE subject = 'history'""")

        elif history == 3:
            c.execute("""UPDATE grades SET count_3 = count_3 + 1 WHERE subject = 'history'""")

        elif history == 2:
            c.execute("""UPDATE grades SET count_2 = count_2 + 1 WHERE subject = 'history'""")

        if english_lang == 5:
            c.execute("""UPDATE grades SET count_5 = count_5 + 1 WHERE subject = 'english_lang'""")

        elif english_lang == 4:
            c.execute("""UPDATE grades SET count_4 = count_4 + 1 WHERE subject = 'english_lang'""")

        elif english_lang == 3:
            c.execute("""UPDATE grades SET count_3 = count_3 + 1 WHERE subject = 'english_lang'""")


        elif english_lang == 2:
            c.execute("""UPDATE grades SET count_2 = count_2 + 1 WHERE subject = 'english_lang'""")


        db.commit()
    db.close()


# здесь вызывать при дропе таблицы   
'''
with sqlite3.connect('examenation.db') as db:
    c = db.cursor()

    c.execute("INSERT INTO grades VALUES ('math', '0', '0', '0', '0')")
    c.execute("INSERT INTO grades VALUES ('programming', '0', '0', '0', '0')")
    c.execute("INSERT INTO grades VALUES ('discrete_math', '0', '0', '0', '0')")
    c.execute("INSERT INTO grades VALUES ('history', '0', '0', '0', '0')")
    c.execute("INSERT INTO grades VALUES ('english_lang', '0', '0', '0', '0')")

'''



thisTable = int(input("Выберите таблицу для взаимодействия с данными:\n 1. Предметы\n 2. Оценки\n 3. Студенты\n(!): "))

if thisTable == 1:

    doing = int(input("Выберите действие с таблицей:\n 1. Добавление данных\n 2. Удаление данных\n 3. Выбор данных\n(!): "))

    if doing == 1:

        with sqlite3.connect('examenation.db') as db:

            c = db.cursor()

            subject = input("Введите название предмета: ") or "None"
            hours = int(input("Введите количество часов: ")) or "None"
            teacher = input("Введите Фамилию И.О преподавателя: ") or "None"
            exam_view = input("Введите вид экзамена (диф. зачет/экзамен): ") or "None"
            time = input("Введите время проведения экзамена в формате HH:MM: ") or "00:00"
            audience = int(input("Введите номер аудитории проведения экзамена: ")) or "None"

            c.execute(f"INSERT INTO lessons VALUES ('{subject}', '{hours}', '{teacher}', '{exam_view}', '{time}', '{audience}')")
            db.commit()
        db.close()

    elif doing == 2:

        for_remove = input("Введите предмет для удаления: ")

        with sqlite3.connect('examenation.db') as db:

            c = db.cursor()

            c.execute(f"DELETE FROM lessons WHERE subject = '{for_remove}'")
            db.commit()
        db.close()

    elif doing == 3:

        given = input("Введите предмет по которому хотите получить информацию: ")

        with sqlite3.connect("examenation.db") as db:

            c = db.cursor()

            info = c.execute("SELECT * FROM lessons").fetchall()

            for value in info:
                print("----------")
                print(f"Предмет: {value[0]}")
                print(f"Часы: {value[1]}")
                print(f"Преподаватель: {value[2]}")
                print(f"Вид экзамена: {value[3]}")
                print(f"Время проведения: {value[4]}")
                print(f"Аудитория: {value[5]}")
                print("----------")

            db.commit()
        db.close()

if thisTable == 3:

    doing = int(input("Выберите действие с таблицей:\n 1. Добавление данных\n 2. Удаление данных\n 3. Выбор данных\n(!): "))

    if doing == 1:

        with sqlite3.connect('examenation.db') as db:

            c = db.cursor()

            name = input("Введите имя студента: ") or "None"
            group_name = input("Введите название группы: ") or "None"
            math = int(input("Введите оценку по высшей математике: ")) or "0"
            programming = int(input("Введите оценку по программированию: ")) or "0"
            discrete_math = int(input("Введите оценку по дискретной математике: ")) or "0"
            history = int(input("Введите оценку по истории: ")) or "0"
            english_lang = int(input("Введите оценку по английскому языку: ")) or "0"

            update_counter(math, programming, discrete_math, history, english_lang)
            

            c.execute(f"INSERT INTO students VALUES ('{name}', '{group_name}', '{math}', '{programming}', '{discrete_math}', '{history}', '{english_lang}')")

            

            db.commit()
        db.close()

    elif doing == 2:

        with sqlite3.connect('examenation.db') as db:
            c = db.cursor()
            namedelete = input("Введите имя студента чью успеваемость нужно очистить: ")
            c.execute(f"DELETE FROM students WHERE name = '{namedelete}'")
            db.commit()
        db.close()

    elif doing == 3:

        name = input("Введите имя студента чью инфорамцию вывести: ")

        with sqlite3.connect('examenation.db') as db:
            c = db.cursor()

            info = c.execute(f"SELECT * FROM students WHERE name = '{name}'").fetchall()
            print("---------")

            for row in info:
                print(f"Имя студента: {row[0]}")
                print(f"Номер группы: {row[1]}")
                print(f"Высшая математика: {row[2]}")
                print(f"Программирование: {row[3]}")
                print(f"Дискретная математика: {row[4]}")
                print(f"История: {row[5]}")
                print(f"Английский язык: {row[6]}")
            
            print("---------")
            db.commit()
        db.close()