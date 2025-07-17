# ProjectSearchforvacancies

Курсовой проект по интеграции с API hh.ru.  
Позволяет искать вакансии, сохранять в JSON, фильтровать, сортировать и взаимодействовать через консоль.

---

## 🔧 Стек технологий

- Python 3.11
- [HH.ru API](https://github.com/hhru/api)
- Poetry
- requests
- pytest, flake8, black, isort, mypy
- pre-commit

---

## 🚀 Возможности

- Поиск вакансий по ключевому слову через hh.ru API
- Сохранение в JSON (без дублей)
- Фильтрация по описанию
- Сортировка по зарплате
- Получение Top N вакансий
- Консольный интерфейс
- Покрытие тестами

---

## 🔄 Установка


git clone https://github.com/your-username/projectsearchforvacancies.git
cd projectsearchforvacancies
poetry install
poetry shell


▶️ Запуск

python main.py


✅ Тесты

pytest

Pre-commit хуки

pre-commit install
pre-commit run --all-files



Структура
.
├── api/               # Работа с API (абстрактный и HH API)
├── models/            # Класс Vacancy
├── storage/           # JSON хранилище + абстрактный класс
├── utils/             # Хелперы для фильтрации и сортировки
├── tests/             # Pytest-модули
├── main.py            # Точка входа
├── pyproject.toml     # Poetry конфигурация
├── .pre-commit-config.yaml
├── .flake8
├── mypy.ini
├── README.md
└── .gitignore



👨‍💻 Автор
Artem Kabritskii
artemkabr7@gmail.com


