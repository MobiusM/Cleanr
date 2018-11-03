from handlers import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler
from emoji import emojize

COMMAND_NAME = 'thot'


class ThotHandler(BaseHandler):

    @staticmethod
    def __thot(bot: Bot, update: Update):
        """
        Thot.
        """
        update.message.reply_text(
            emojize(':eggplant::peach:'))

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, ThotHandler.__thot)
