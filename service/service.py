from typing import Dict, List

from repository import repository


def get_coursers() -> List:
    res = repository.get_coursers()
    list_courses = [i[0] for i in res]
    return list_courses
