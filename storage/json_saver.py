# storage/json_saver.py
import json
import os
from typing import List

from models.vacancy import Vacancy
from storage.abstract_storage import AbstractStorage


class JSONSaver(AbstractStorage):
    """
    Класс для работы с JSON-файлом: сохранение, удаление и фильтрация вакансий.
    """

    def __init__(self, file_name: str = "vacancies.json") -> None:
        self.__file_name = file_name

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в JSON-файл. Повторные записи не сохраняются.
        """
        vacancies = self.get_all_vacancies()

        if not any(v.url == vacancy.url for v in vacancies):
            vacancies.append(vacancy)

        self.__write_to_file(vacancies)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии по ссылке.
        """
        vacancies = self.get_all_vacancies()
        vacancies = [v for v in vacancies if v.url != vacancy.url]
        self.__write_to_file(vacancies)

    def get_all_vacancies(self) -> List[Vacancy]:
        """
        Получить все вакансии из файла.
        """
        if not os.path.exists(self.__file_name):
            return []

        with open(self.__file_name, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return [Vacancy.from_dict(v) for v in data]
            except json.JSONDecodeError:
                return []

    def get_vacancies_by_keyword(self, keyword: str) -> List[Vacancy]:
        """
        Получить вакансии, содержащие ключевое слово в описании.
        """
        return [
            v
            for v in self.get_all_vacancies()
            if keyword.lower() in v.description.lower()
        ]

    def __write_to_file(self, vacancies: List[Vacancy]) -> None:
        """
        Приватный метод для записи списка вакансий в файл.
        """
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(
                [v.to_dict() for v in vacancies], file, ensure_ascii=False, indent=2
            )
