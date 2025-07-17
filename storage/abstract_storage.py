# storage/abstract_storage.py
from abc import ABC, abstractmethod
from typing import List

from models.vacancy import Vacancy


class AbstractStorage(ABC):
    """
    Абстрактный класс для всех хранилищ вакансий.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_all_vacancies(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def get_vacancies_by_keyword(self, keyword: str) -> List[Vacancy]:
        pass
