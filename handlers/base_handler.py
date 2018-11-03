from abc import abstractmethod


class BaseHandler:

    @staticmethod
    @abstractmethod
    def get_handler():
        pass
