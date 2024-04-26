import json

import pytest
from src.Vacancy import Vacancy


def test_init():
    # Тестируем инициализацию объекта с корректными данными
    vacancy = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    assert vacancy.name == "Test name"
    assert vacancy.url == "https://test.url"
    assert vacancy.salary == {"from": 1000, "to": 2000}

    # Тестируем инициализацию объекта без данных о зарплате
    vacancy = Vacancy("Test name", "https://test.url")
    assert vacancy.name == "Test name"
    assert vacancy.url == "https://test.url"
    assert vacancy.salary is None

    # Тестируем инициализацию объекта с некорректными данными о зарплате
    with pytest.raises(ValueError):
        Vacancy("Test name", "https://test.url", "Invalid salary")


def test_cast_to_object_list():
    # Тестируем преобразование данных в список объектов
    data = {
        "items": [
            {"name": "Test name 1", "alternate_url": "https://test.url1", "salary": {"from": 1000, "to": 2000}},
            {"name": "Test name 2", "alternate_url": "https://test.url2", "salary": None},
            {"name": "Test name 3", "alternate_url": "https://test.url3", "salary": {"from": 3000, "to": 4000}}
        ]
    }
    vacancies = Vacancy.cast_to_object_list(data)
    assert len(vacancies) == 2
    assert vacancies[0].name == "Test name 1"
    assert vacancies[0].url == "https://test.url1"
    assert vacancies[0].salary == {"from": 1000, "to": 2000}
    assert vacancies[1].name == "Test name 3"
    assert vacancies[1].url == "https://test.url3"
    assert vacancies[1].salary == {"from": 3000, "to": 4000}


def test_to_dict():
    # Тестируем преобразование объекта в словарь
    vacancy = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    vacancy_dict = vacancy.to_dict()
    assert vacancy_dict == {"name": "Test name", "url": "https://test.url", "salary": {"from": 1000, "to": 2000}}


def test_str():
    # Тестируем вывод объекта в виде строки
    vacancy = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    assert str(vacancy) == "Test name - https://test.url - от 1000 до 2000"

    vacancy = Vacancy("Test name", "https://test.url", {"from": 1000, "to": None})
    assert str(vacancy) == "Test name - https://test.url - от 1000"

    vacancy = Vacancy("Test name", "https://test.url", {"from": None, "to": 2000})
    assert str(vacancy) == "Test name - https://test.url - до 2000"

    vacancy = Vacancy("Test name", "https://test.url", None)
    assert str(vacancy) == "Test name - https://test.url - зарплата не указана"


def test_from_dict():
    # Тестируем преобразование словаря в объект
    vacancy_dict = {"name": "Test name", "url": "https://test.url", "salary": {"from": 1000, "to": 2000}}
    vacancy = Vacancy.from_dict(json.dumps(vacancy_dict))
    assert vacancy.name == "Test name"
    assert vacancy.url == "https://test.url"
    assert vacancy.salary == {"from": 1000, "to": 2000}


def test_eq():
    # Тестируем сравнение объектов
    vacancy1 = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    vacancy2 = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    vacancy3 = Vacancy("Test name", "https://test.url", {"from": 2000, "to": 3000})
    assert vacancy1 == vacancy2
    assert vacancy1 != vacancy3


def test_ge():
    # Тестируем сравнение объектов "больше или равно"
    vacancy1 = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    vacancy2 = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    vacancy3 = Vacancy("Test name", "https://test.url", {"from": 2000, "to": 3000})
    assert vacancy1 >= vacancy2
    assert vacancy1 < vacancy3


def test_gt():
    # Тестируем сравнение объектов "больше"
    vacancy1 = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    vacancy2 = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    vacancy3 = Vacancy("Test name", "https://test.url", {"from": 2000, "to": 3000})
    assert not vacancy1 > vacancy2
    assert vacancy3 > vacancy1


if __name__ == "__main__":
    pytest.main()