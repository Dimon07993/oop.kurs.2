from abc import ABC, abstractmethod


class DataStorage(ABC):
    @abstractmethod
    def add_vacancy(self, data):
        pass

    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
