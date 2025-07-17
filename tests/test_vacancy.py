from models.vacancy import Vacancy


def test_vacancy_creation() -> None:
    v = Vacancy("Test", "http://example.com", 100000, 150000, "описание")
    assert v.salary_from == 100000
    assert v.salary_to == 150000


def test_salary_validation() -> None:
    v = Vacancy("Test", "url", None, -10, "")
    assert v.salary_from == 0
    assert v.salary_to == 0


def test_comparison() -> None:
    v1 = Vacancy("1", "u1", 50000, 60000, "")
    v2 = Vacancy("2", "u2", 100000, 110000, "")
    assert v1 < v2
    assert v2 > v1
    assert not v1 == v2


def test_dict_conversion() -> None:
    v = Vacancy("T", "u", 10, 20, "d")
    d = v.to_dict()
    v2 = Vacancy.from_dict(d)
    assert v2.title == "T"
