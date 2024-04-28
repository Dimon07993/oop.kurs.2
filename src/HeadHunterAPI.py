from src.APIConnector import APIConnector
import requests


class HeadHunterAPI(APIConnector):
    def __init__(self):
        pass

    def get_vacancies(self, keyword=None, page=None, salary=None):
        """Подключение к API HeadHunter и получение списка вакансий по ключевому слову"""
        url = 'https://api.hh.ru/vacancies'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        params = {
            'text': keyword,
            'per_page': page,
            'salary': salary,

        }

        response = requests.get(url.strip(), headers=headers, timeout=10, params=params).json()

        return response

    def connection_to_api(self):
        pass
