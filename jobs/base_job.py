from abc import abstractmethod


class BaseJob:

    @staticmethod
    @abstractmethod
    def set_job(job_queue):
        pass
