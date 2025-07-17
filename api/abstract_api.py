# api/abstract_api.py
from abc import ABC, abstractmethod
from typing import Dict, List


class AbstractAPI(ABC):
    """
    Абстрактный класс для API-сервисов вакансий.
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Получить список вакансий по ключевому слову.
        """
        pass
