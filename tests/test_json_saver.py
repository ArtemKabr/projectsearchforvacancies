from pathlib import Path

from models.vacancy import Vacancy
from storage.json_saver import JSONSaver


def test_add_vacancy(tmp_path: Path) -> None:
    file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file))
    vacancy = Vacancy("Test", "http://url", 100000, 120000, "desc")
    saver.add_vacancy(vacancy)
    data = saver.get_all_vacancies()
    assert len(data) == 1


def test_get_vacancies(tmp_path: Path) -> None:
    file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file))
    vacancy = Vacancy("Test", "http://url", 100000, 120000, "desc")
    saver.add_vacancy(vacancy)
    result = saver.get_all_vacancies()
    assert isinstance(result, list)
    assert result[0].title == "Test"


def test_delete_vacancy(tmp_path: Path) -> None:
    file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file))
    vacancy = Vacancy("Test", "http://url", 100000, 120000, "desc")
    saver.add_vacancy(vacancy)
    saver.delete_vacancy(vacancy)
    assert len(saver.get_all_vacancies()) == 0
