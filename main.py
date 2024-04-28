import requests
import json

from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy
from src.HeadHunterAPI import HeadHunterAPI
from requests.auth import HTTPProxyAuth

hh_api = HeadHunterAPI()

hh_vacancies = hh_api.get_vacancies(keyword='python', page=100)

vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)


def user_interaction():
    platforms = ["HeadHunter"]
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    ranged_vacancies = Vacancy.get_vacancies_by_salary(vacancies_list, salary_range)
    top_vacancies = Vacancy.get_top_vacancies(ranged_vacancies, top_n)

    for top_vacancy in top_vacancies:
        print(top_vacancy)


if __name__ == '__main__':
    user_interaction()




# hh_vacancies = hh_api.get_vacancies(input('введите ключевое слово: '), int(input('введите количество вакансий: ')),
#                                     int(input('введите запрос по зарплате: ')))
#
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
# for i in vacancies_list:
#     print(i)
#
# vacancy = Vacancy('Python разработчик111', 'https://hh.ru/vacancy/954471839', {'from': 100000, 'to': 200000})
# print(vacancy)
#
# json_saver = JSONSaver('data/hh1.json')
# json_saver.add_vacancy(vacancy)
# vacancy1 = Vacancy('P999', 'https://hh.ru/vacancy/954471831', {'from': 100000, 'to': 200000})
# json_saver.add_vacancy(vacancy1)
# vacancy1 = Vacancy('984695ыва', 'https://hh.ru/vacancy/954471832', {'from': 100000, 'to': 200000})
# json_saver.add_vacancy(vacancy1)
# vacancy2 = Vacancy('Python разработчик1112', 'https://hh.ru/vacancy/9544718395', {'from': 100000, 'to': 200000})
# vacancy3 = Vacancy('Python разработчик1113', 'https://hh.ru/vacancy/9544718396', {'from': 1000000, 'to': 200000})
#
# if vacancy2 >= vacancy3:
#     print(Vacancy.__eq__(vacancy2, vacancy3))
#     print('yes')
# else:
#     print('no')

#
#
# vacancy2 = Vacancy('77777', 'https://hh.ru/vacancy/77777777777', {'from': 100000, 'to': 200000})
# # json_saver.add_vacancy(vacancy2)
# json_saver.delete_vacancy(vacancy2)


# if __name__ == '__main__':
#     user_interaction()
