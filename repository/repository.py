import sqlite3
from typing import List


conn = sqlite3.connect("repository/dekanat.db")
cursor = conn.cursor()


def get_all_users_student() -> (List, bool):
    try:
        cursor.execute("select id, lastName, firstName, middleName, directionEducation, numberGroup from students")
        users_data = cursor.fetchall()
        return reversed(users_data), True

    except sqlite3.Error:
        return [], False


def get_all_users_student_filter_search_line(substring: str) -> (List, bool):
    try:
        cursor.execute("select id, lastName, firstName, middleName, directionEducation, numberGroup "
                       "from students where lastName like ?", (substring, ))
        users_data = cursor.fetchall()
        return reversed(users_data), True

    except sqlite3.Error:
        return [], False


def get_all_users_teacher() -> List:
    pass


def get_user_student(user_id: int) -> (List, bool):
    try:
        cursor.execute("select * from students where id = ? ", (user_id, ))
        user_data = cursor.fetchall()
        return user_data, True

    except sqlite3.Error:
        return [], False


def update_user_student(user_data: List) -> bool:
    pass


def set_user_student(user_data: List) -> bool:
    try:
        cursor.execute("insert into students(lastname, firstname, middlename, formeducation, course, directioneducation, "
                       "numbergroup, birthday, passportid, login, password) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(user_data))
        conn.commit()
        return True

    except sqlite3.Error as e:
        print(e)
        return False


def delete_user_student(user_id: int) -> bool:
    try:
        cursor.execute("delete from students where id = ?", (user_id, ))
        conn.commit()
        return True

    except sqlite3.Error as e:
        print(e)
        return False


def _init_repository():
    with open("repository/schema.sql", encoding='utf-8') as f:
        sql = f.read()
        print(sql)
    cursor.executescript(sql)
    conn.commit()


def _check_repository_exists():
    cursor.execute("select name from sqlite_master where type = 'table'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_repository()


_check_repository_exists()
