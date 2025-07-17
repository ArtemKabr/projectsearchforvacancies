# api/hh_api.py
from typing import Dict, List

import requests  # type: ignore

from api.abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "VacancySearchApp"}
        self.__per_page = 20

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Получение вакансий с hh.ru по ключевому слову.
        """
        vacancies = []
        for page in range(self.__per_page):
            params: dict[str, str] = {
                "text": keyword,
                "page": str(page),
                "per_page": "100",
            }
            response = requests.get(self.__url, headers=self.__headers, params=params)
            if response.status_code != 200:
                break
            data = response.json().get("items", [])
            if not data:
                break
            vacancies.extend(data)
        return vacancies
