import pytest

from src.HeadHunterAPI import HeadHunterAPI


def test_get_vacancies():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies('python', 10, 100000)
    assert len(hh_vacancies) == 10


if __name__ == '__main__':
    pytest.main()
