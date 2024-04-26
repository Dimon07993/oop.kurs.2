import os

import pytest
import json

from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy


def test_add_vacancy():
    # Удаляем тестовый JSON-файл, если он существует
    if os.path.exists("test.json"):
        os.remove("test.json")
    # Тестируем добавление вакансии в JSON-файл
    saver = JSONSaver("test.json")
    vacancy = Vacancy("Test name", "https://test.url", {"from": 1000, "to": 2000})
    saver.add_vacancy(vacancy)

    with open("test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["name"] == "Test name"
    assert data[0]["url"] == "https://test.url"
    assert data[0]["salary"] == {"from": 1000, "to": 2000}

    # Тестируем добавление вакансии, которая уже есть в JSON-файле
    saver.add_vacancy(vacancy)
    with open("test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1


def test_delete_vacancy():
    # Удаляем тестовый JSON-файл, если он существует
    if os.path.exists("test.json"):
        os.remove("test.json")
    # Тестируем удаление вакансии из JSON-файла
    saver = JSONSaver("test.json")
    vacancy1 = Vacancy("Test name 1", "https://test.url1", {"from": 1000, "to": 2000})
    vacancy2 = Vacancy("Test name 2", "https://test.url2", {"from": 3000, "to": 4000})
    saver.add_vacancy(vacancy1)
    saver.add_vacancy(vacancy2)

    with open("test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 2

    saver.delete_vacancy(vacancy1)
    with open("test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["name"] == "Test name 2"
    assert data[0]["url"] == "https://test.url2"
    assert data[0]["salary"] == {"from": 3000, "to": 4000}

    # Тестируем удаление вакансии, которой нет в JSON-файле
    saver.delete_vacancy(vacancy1)
    with open("test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1


if __name__ == "__main__":
    pytest.main()
