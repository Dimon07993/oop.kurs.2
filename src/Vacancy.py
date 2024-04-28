import json


class Vacancy:
    def __init__(self, name, url, salary=None):
        """Инициализация вакансий"""
        if salary is not None and not isinstance(salary, dict):
            raise ValueError(f'Словарь с данными о зарплате должен быть типа словарь, а не {type(salary)}')
        self.name = name
        self.url = url
        self.salary = salary

    @staticmethod
    def cast_to_object_list(data):
        """Преоброзование данных в список объектов"""
        return [Vacancy(i['name'], i['alternate_url'], i['salary']) for i in data['items'] if i['salary'] is not None]

    def to_dict(self):
        """Преоброзование данных в словарь"""
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary
        }

    def __str__(self):
        """Вывод вакансий"""
        if self.salary is not None:
            if self.salary['from'] is not None and self.salary['to'] is not None:
                return f'{self.name} - {self.url} - от {self.salary["from"]} до {self.salary["to"]}'

            elif self.salary['from'] is not None:
                return f'{self.name} - {self.url} - от {self.salary["from"]}'

            elif self.salary['to'] is not None:
                return f'{self.name} - {self.url} - до {self.salary["to"]}'
        else:
            return f'{self.name} - {self.url} - зарплата не указана'

    @classmethod
    def from_dict(cls, data):
        """Преоброзование словаря в объект"""
        data = json.loads(data)
        return cls(data['name'], data['url'], data['salary'])

    @staticmethod
    def get_vacancies_by_salary(vacancies_list, salary_range):
        """Фильтрация вакансий по зарплате"""
        salary_from, salary_to = salary_range.split('-')
        ranged_vacancies = []
        for i in vacancies_list:
            if i.salary.get('from') is not None and int(i.salary.get('from')) >= int(salary_from):
                if i.salary.get('to') is not None and int(i.salary.get('to')) <= int(salary_to):
                    ranged_vacancies.append(i)
                elif i.salary.get('to') is None:
                    ranged_vacancies.append(i)

        return ranged_vacancies

    @staticmethod
    def get_top_vacancies(ranged_vacancies, top_n):
        """Получение топ N вакансий"""
        return sorted(ranged_vacancies, key=lambda x: x.salary['from'], reverse=True)[:top_n]

    def __eq__(self, other):
        """Сравнение вакансий"""
        return self.salary == other.salary

    def __ge__(self, other):
        """Сравнение вакансий"""
        if self.salary["from"] > other.salary["from"]:
            return True
        if self.salary["from"] < other.salary["from"]:
            return False
        if self.salary["to"] > other.salary["to"]:
            return True
        if self.salary["to"] < other.salary["to"]:
            return False
        return True

    def __gt__(self, other):
        """Сравнение вакансий"""
        if self.salary["from"] > other.salary["from"]:
            return True
        if self.salary["from"] < other.salary["from"]:
            return False
        if self.salary["to"] > other.salary["to"]:
            return True
        if self.salary["to"] < other.salary["to"]:
            return False
        return False
