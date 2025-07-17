# utils/helpers.py
from typing import List

from models.vacancy import Vacancy


def filter_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """
    Фильтрация вакансий по ключевому слову в описании.
    """
    return [v for v in vacancies if keyword.lower() in v.description.lower()]


def sort_vacancies_by_salary(
    vacancies: List[Vacancy], reverse: bool = True
) -> List[Vacancy]:
    """
    Сортировка вакансий по нижней границе зарплаты.
    """
    return sorted(vacancies, key=lambda v: v.salary_from, reverse=reverse)


def get_top_n_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """
    Получение топ N вакансий по зарплате.
    """
    return vacancies[:n]
