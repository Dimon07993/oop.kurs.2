from abc import ABC, abstractmethod


class APIConnector(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def connection_to_api(self):
        pass


