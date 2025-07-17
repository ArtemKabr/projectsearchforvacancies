from typing import List

from models.vacancy import Vacancy
from utils.helpers import (filter_by_keyword, get_top_n_vacancies,
                           sort_vacancies_by_salary)


def get_sample_vacancies() -> List[Vacancy]:
    return [
        Vacancy("Python Dev", "url1", 100000, 150000, "Python developer"),
        Vacancy("Java Dev", "url2", 80000, 120000, "Java developer"),
        Vacancy("C++ Dev", "url3", 90000, 130000, "C++ developer"),
    ]


def test_filter_by_keyword() -> None:
    vacancies = get_sample_vacancies()
    filtered = filter_by_keyword(vacancies, "Python")
    assert len(filtered) == 1
    assert filtered[0].title == "Python Dev"


def test_sort_vacancies_by_salary() -> None:
    vacancies = get_sample_vacancies()
    sorted_vacancies = sort_vacancies_by_salary(vacancies)
    assert sorted_vacancies[0].title == "Python Dev"


def test_get_top_n_vacancies() -> None:
    vacancies = get_sample_vacancies()
    top_2 = get_top_n_vacancies(vacancies, 2)
    assert len(top_2) == 2
    assert top_2[0].salary_from >= top_2[1].salary_from
