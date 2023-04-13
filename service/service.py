from typing import Dict, List

from repository import repository


def get_all_users_students(flag: str) -> List:
    users_data, err = repository.get_all_users_student(flag)
    if not err:
        return []

    response = []
    for value in users_data:
        user_data = []
        for i in value:
            user_data.append(i)
        response.append(user_data)
    return response


def get_all_users_teacher(flag: str) -> List:
    users_data, err = repository.get_all_users_teacher(flag)
    if not err:
        return []

    response = []
    for value in users_data:
        user_data = []
        for i in value:
            user_data.append(i)
        response.append(user_data)
    return response


def get_all_users_filter_search_line(substring: str, type_user: str) -> List:
    users_data, err = repository.get_all_users_filter_search_line(substring, type_user)
    if not err:
        return []
    response = []
    for value in users_data:
        user_data = []
        for i in value:
            user_data.append(i)
        response.append(user_data)
    return response


def delete_user(user_id: int, type_user: str) -> bool:
    return repository.delete_user(user_id, type_user)


def get_user_full_data(user_id: int, type_user: str) -> (List, bool):
    res, err = repository.get_user(user_id, type_user)
    if not err:
        return [], err

    user_data = []
    for value in res[0]:
        user_data.append(value)
    return user_data, err


def set_user_data(user_data: List, type_user: str) -> bool:
    return repository.set_user_data(user_data, type_user)


def update_user(user_data: List, type_user: str) -> bool:
    return repository.update_user(user_data, type_user)


def set_users_student_pull(users_data: List) -> bool:
    for value in users_data:
        res = repository.set_user_data(value, "student")
        if not res:
            return False
    return True


def get_rating(user_id: int) -> (Dict, bool):
    rating_data, err = repository.get_rating(user_id)
    if not err:
        return {}, False

    res = {}
    for i in rating_data:
        if i[0] not in res:
            res[i[0]] = []

    for i in rating_data:
        res[i[0]].append(i[1:])

    return res, True


def update_rate(rate_data: List) -> bool:
    return repository.update_rate(rate_data)


def check_user(login: str, password: str, type_user: str) -> (str, bool):
    return repository.check_user(login, password, type_user)
