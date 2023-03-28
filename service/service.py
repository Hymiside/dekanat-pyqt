from typing import Dict, List, Tuple

from repository import repository


def get_all_users_students() -> List:
    users_data, err = repository.get_all_users_student()
    if not err:
        return []
    response = []
    for value in users_data:
        user_data = []
        for i in value:
            user_data.append(i)
        response.append(user_data)
    return response


def get_all_users_students_filter_search_line(substring: str) -> List:
    users_data, err = repository.get_all_users_student_filter_search_line(substring)
    if not err:
        return []
    response = []
    for value in users_data:
        user_data = []
        for i in value:
            user_data.append(i)
        response.append(user_data)
    return response


def delete_user_student(user_id: int) -> bool:
    res = repository.delete_user_student(user_id)
    return res


def get_all_users_teacher() -> List:
    pass


def get_user_student(user_id: int) -> (List, bool):
    res, err = repository.get_user_student(user_id)
    if not err:
        return [], err

    user_data = []
    for value in res[0]:
        user_data.append(value)
    return user_data, err


def set_user_student(user_data: List) -> bool:
    res = repository.set_user_student(user_data)
    return res


def set_users_student_pull(users_data: List) -> bool:
    for value in users_data:
        res = repository.set_user_student(value)
        if not res:
            return False
    return True
