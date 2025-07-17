# models/vacancy.py
from functools import total_ordering
from typing import Any, Dict, Optional


@total_ordering
class Vacancy:
    __slots__ = ("title", "url", "salary_from", "salary_to", "description")

    def __init__(
        self,
        title: str,
        url: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        description: str,
    ) -> None:
        self.title = title
        self.url = url
        self.salary_from = self.__validate_salary(salary_from)
        self.salary_to = self.__validate_salary(salary_to)
        self.description = description.strip() if description else "Описание не указано"

    def __validate_salary(self, salary: Optional[int]) -> int:
        if isinstance(salary, int) and salary > 0:
            return salary
        return 0

    def __repr__(self) -> str:
        return (
            f"{self.title} | от {self.salary_from} до {self.salary_to} руб.\n{self.url}"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from == other.salary_from

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from < other.salary_from

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Vacancy":
        return cls(
            title=data.get("title", "Не указано"),
            url=data.get("url", ""),
            salary_from=data.get("salary_from"),
            salary_to=data.get("salary_to"),
            description=data.get("description", ""),
        )
