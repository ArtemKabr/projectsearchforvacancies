from typing import Any

from api.hh_api import HeadHunterAPI
from models.vacancy import Vacancy
from storage.json_saver import JSONSaver
from utils.helpers import (filter_by_keyword, get_top_n_vacancies,
                           sort_vacancies_by_salary)


def user_interaction() -> None:
    """
    Функция взаимодействия с пользователем через консоль.
    """
    api = HeadHunterAPI()
    storage = JSONSaver()

    print("=== Поиск вакансий на hh.ru ===")
    query: str = input("Введите поисковый запрос: ").strip()

    print("Загружаем вакансии...")
    raw_vacancies: list[dict[str, Any]] = api.get_vacancies(query)

    vacancies: list[Vacancy] = []
    for item in raw_vacancies:
        vacancy = Vacancy(
            title=str(item.get("name") or ""),
            url=str(item.get("alternate_url") or ""),
            salary_from=(item.get("salary") or {}).get("from"),
            salary_to=(item.get("salary") or {}).get("to"),
            description=(item.get("snippet") or {}).get("requirement") or "",
        )
        storage.add_vacancy(vacancy)
        vacancies.append(vacancy)

    print(f"Найдено {len(vacancies)} вакансий.")

    keyword: str = input("Введите ключевое слово для фильтрации по описанию: ").strip()
    filtered: list[Vacancy] = filter_by_keyword(vacancies, keyword)

    sorted_vacancies: list[Vacancy] = sort_vacancies_by_salary(filtered)

    try:
        top_n: int = int(input("Введите количество топ-вакансий по зарплате: "))
    except ValueError:
        top_n = 5

    top: list[Vacancy] = get_top_n_vacancies(sorted_vacancies, top_n)

    print(f"\nТоп {top_n} вакансий по зарплате с ключевым словом '{keyword}':\n")
    for vacancy in top:
        print(vacancy)
        print("-" * 80)


if __name__ == "__main__":
    user_interaction()
