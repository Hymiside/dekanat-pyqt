import sqlite3
from typing import List


conn = sqlite3.connect("repository/dekanat.db")
cursor = conn.cursor()


def get_all_users_student(flag: str) -> (List, bool):
    match flag:
        case "preview":
            try:
                cursor.execute("select id, lastName, firstName, middleName, directionEducation, numberGroup from students")
                users_data = cursor.fetchall()
                return reversed(users_data), True

            except sqlite3.Error:
                return [], False

        case "full":
            try:
                cursor.execute("select lastName, firstName, middleName, formEducation, course, directionEducation, "
                               "numberGroup, birthday, passportID, login, password from students")
                users_data = cursor.fetchall()
                return reversed(users_data), True

            except sqlite3.Error:
                return [], False


def get_all_users_teacher(flag: str) -> (List, bool):
    match flag:
        case "preview":
            try:
                cursor.execute(
                    "select id, lastName, firstName, middleName, department from teachers")
                users_data = cursor.fetchall()
                return reversed(users_data), True

            except sqlite3.Error:
                return [], False

        case "full":
            try:
                cursor.execute("select lastName, firstName, middleName, department, subject, birthday, "
                               "email, password from teachers")
                users_data = cursor.fetchall()
                return reversed(users_data), True

            except sqlite3.Error:
                return [], False


def get_all_users_filter_search_line(substring: str, type_user: str) -> (List, bool):
    match type_user:
        case "student":
            try:
                cursor.execute("select id, lastName, firstName, middleName, directionEducation, numberGroup "
                               "from students where lastName like ?", (substring, ))
                users_data = cursor.fetchall()
                return reversed(users_data), True

            except sqlite3.Error:
                return [], False
        case "teacher":
            try:
                cursor.execute("select id, lastName, firstName, middleName, department "
                               "from teachers where lastName like ?", (substring,))
                users_data = cursor.fetchall()
                return reversed(users_data), True

            except sqlite3.Error:
                return [], False


def get_user(user_id: int, type_user: str) -> (List, bool):
    match type_user:
        case "student":
            try:
                cursor.execute("select * from students where id = ? ", (user_id,))
                user_data = cursor.fetchall()
                return user_data, True

            except sqlite3.Error:
                return [], False

        case "teacher":
            try:
                cursor.execute("select * from teachers where id = ? ", (user_id, ))
                user_data = cursor.fetchall()
                return user_data, True

            except sqlite3.Error:
                return [], False


def update_user(user_data: List, type_user: str) -> bool:
    match type_user:
        case "student":
            try:
                cursor.execute("update students set lastName = ?, firstName = ?, middleName = ?, formEducation = ?,"
                               "course = ?, directionEducation = ?, numberGroup = ?, birthday = ?, passportID = ? where id = ?", tuple(user_data))
                conn.commit()
                return True
            except sqlite3.Error as e:
                print(e)
                return False

        case "teacher":
            try:
                cursor.execute("update teachers set lastName = ?, firstName = ?, middleName = ?, department = ?,"
                               "subject = ?, birthday = ?, email = ? where id = ?", tuple(user_data))
                conn.commit()
                return True
            except sqlite3.Error as e:
                print(e)
                return False


def set_user_data(user_data: List, type_user: str) -> bool:


    match type_user:
        case "student":
            try:
                user_id = cursor.execute("insert into students(lastname, firstname, middlename, formeducation, course, directioneducation, "
                                         "numbergroup, birthday, passportid, login, password) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) returning id", tuple(user_data)).fetchone()
                conn.commit()

                data = [
                    (user_id[0], 'Аналитическая геометрия', 'КТ1', '13', '30'),
                    (user_id[0], 'Аналитическая геометрия', 'КТ2', '13', '30'),
                    (user_id[0], 'Аналитическая геометрия', 'КТ3', '13', '30'),
                    (user_id[0], 'Аналитическая геометрия', 'КТ4', '13', '30'),
                    (user_id[0], 'Аналитическая геометрия', 'КТ5', '13', '30'),
                    (user_id[0], 'Математический анализ', 'КТ1', '13', '30'),
                    (user_id[0], 'Математический анализ', 'КТ2', '13', '30'),
                    (user_id[0], 'Математический анализ', 'КТ3', '13', '30'),
                    (user_id[0], 'Математический анализ', 'КТ4', '13', '30'),
                    (user_id[0], 'Математический анализ', 'КТ5', '13', '30'),
                    (user_id[0], 'АиП', 'КТ1', '13', '30'),
                    (user_id[0], 'АиП', 'КТ2', '13', '30'),
                    (user_id[0], 'АиП', 'КТ3', '13', '30'),
                    (user_id[0], 'Дискретная математика', 'КТ1', '13', '30'),
                    (user_id[0], 'Дискретная математика', 'КТ2', '13', '30'),
                    (user_id[0], 'Дискретная математика', 'КТ3', '13', '30'),
                    (user_id[0], 'Дискретная математика', 'КТ4', '13', '30')]

                for value in data:
                    cursor.execute("insert into ratings (studentId, subject, topic, rate_min, rate_max) values (?, ?, ?, ?, ?)", value)
                    conn.commit()
                return True

            except sqlite3.Error as e:
                print(e)
                return False

        case "teacher":
            try:
                cursor.execute("insert into teachers(lastname, firstname, middlename, department, subject, birthday, "
                               "email, login, password) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(user_data))
                conn.commit()
                return True

            except sqlite3.Error as e:
                print(e)
                return False


def update_rate(rate_data: List) -> bool:
    try:
        cursor.execute("update ratings set rate_real = ? where studentId = ? and topic = ? and subject = ?", tuple(rate_data))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def get_rating(user_id: int) -> (List, bool):
    try:
        rating_data = cursor.execute("select subject, topic, rate_real, rate_min, rate_max from ratings where studentId = ?", (user_id, )).fetchall()
        return rating_data, True
    except sqlite3.Error as e:
        print(e)
        return [], False


def delete_user(user_id: int, type_user: str) -> bool:
    match type_user:
        case "student":
            try:
                cursor.execute("delete from students where id = ?", (user_id,))
                conn.commit()
                cursor.execute("delete from ratings where studentId = ?", (user_id, ))
                conn.commit()
                return True

            except sqlite3.Error as e:
                print(e)
                return False

        case "teacher":
            try:
                cursor.execute("delete from teachers where id = ?", (user_id, ))
                conn.commit()
                return True

            except sqlite3.Error as e:
                print(e)
                return False


def check_user(login: str, password: str, type_user: str) -> (str, bool):
    match type_user:
        case "student":
            try:
                user_id = cursor.execute("select id from students where login = ? and password = ?", (login, password)).fetchone()
                if user_id is not None:
                    return user_id[0], True
                return "Неверный логин или пароль!", False
            except sqlite3.Error as e:
                print(e)
                return "Произошла ошибка! Попробуйте снова.", False

        case "teacher":
            try:
                user_id = cursor.execute("select id from teachers where login = ? and password = ?", (login, password)).fetchone()
                if user_id is not None:
                    return user_id[0], True
                return "Неверный логин или пароль!", False
            except sqlite3.Error as e:
                print(e)
                return "Произошла ошибка! Попробуйте снова.", False


def _init_repository():
    with open("repository/schema.sql", encoding='utf-8') as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def _check_repository_exists():
    cursor.execute("select name from sqlite_master where type = 'table'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_repository()


_check_repository_exists()
