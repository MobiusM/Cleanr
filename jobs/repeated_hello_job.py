from jobs import BaseJob
from telegram.bot import Bot
from telegram.ext import JobQueue, Job

from consts import CLEANING_GROUP_ID

JOB_NAME = 'repeated_hello_job'
JOB_INTERVAL = 60
JOB_FIRST = 0


class RepeatedHelloJob(BaseJob):

    @staticmethod
    def __every_minute(bot: Bot, job: Job):
        """
        Say hello periodically.
        """
        bot.send_message(job.context, "Hello!\nThis is a periodic message.")

    @staticmethod
    def set_job(job_queue: JobQueue):
        return job_queue.run_repeating(RepeatedHelloJob.__every_minute, JOB_INTERVAL, JOB_FIRST,
                                       context=CLEANING_GROUP_ID)
