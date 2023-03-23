from typing import Dict, List

from repository import repository


def get_all_users_students() -> List:
    users_data, err = repository.get_all_users_students()
    if not err:
        return []

    response = []
    for user_data_tuple in users_data:
        user_data_list = []
        for value_user_data in user_data_tuple:
            user_data_list.append(value_user_data)
        response.append(user_data_list)

    return response


def get_all_users_teachers() -> List:
    pass
