import os

from src.DataStorage import DataStorage
from src.Vacancy import Vacancy
import json


class JSONSaver(DataStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancy):
        """Добавления вакансий в JSON файл"""
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        if any(v['url'] == vacancy.url for v in data):
            print(f'Вакансия {vacancy.url} уже есть в JSON файле')
            return

        data.append({
            'name': vacancy.name,
            'url': vacancy.url,
            'salary': vacancy.salary
        })
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_file(self):
        pass

    def delete_vacancy(self, vacancy):
        """Удаление вакансий из JSON файла"""
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        for i in data:
            if i['url'] == vacancy.url:
                data.remove(i)
                with open(self.file_name, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
