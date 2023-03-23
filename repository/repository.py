import sqlite3
from typing import List


conn = sqlite3.connect("repository/dekanat.db")
cursor = conn.cursor()


def get_all_users_students() -> (List, bool):
    try:
        cursor.execute("select id, lastName, firstName, middleName, directionEducation, numberGroup from students")
        users_data = cursor.fetchall()
        return users_data, True
    except:
        return [], False


def get_all_users_teachers() -> List:
    pass


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
