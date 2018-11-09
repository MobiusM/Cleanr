import logging
from typing import List
from jobs import BaseJob
from telegram.ext import JobQueue


class Jobs:
    """
    Super class that governs all jobs.
    """

    def __init__(self, job_queue: JobQueue, repeated_jobs: List[BaseJob] = None):
        self.logger = logging.getLogger(__name__)
        self.job_queue = job_queue
        self.repeated_jobs = repeated_jobs

    def start_jobs(self):
        """
        Start all the available handlers.
        """
        self.__init_repeated_jobs()

    def __init_repeated_jobs(self) -> None:
        """
        Initialize all command handlers.
        """
        if self.repeated_jobs is not None:
            for job in self.repeated_jobs:
                job.set_job(self.job_queue)
        else:
            self.logger.warning('No repeating jobs are enabled.')
