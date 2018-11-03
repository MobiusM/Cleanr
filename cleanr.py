import logging
from telegram.ext import Updater
from handlers import Handlers
from jobs import Jobs

from config import COMMAND_HANDLERS, REPEATING_JOBS


class Cleanr:
    def __init__(self, token):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.updater = Updater(token)
        self.job_queue = self.updater.job_queue
        self.handlers = Handlers(self.updater, command_handlers=COMMAND_HANDLERS)
        self.jobs = Jobs(self.job_queue, repeated_jobs=REPEATING_JOBS)

    def start_bot(self):
        self.handlers.start_handlers()
        self.jobs.start_jobs()

        self.updater.start_polling()
        self.updater.idle()
