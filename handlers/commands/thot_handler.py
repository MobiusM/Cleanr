from handlers.base_handler import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async
from utils import send_typing_action
from emoji import emojize

COMMAND_NAME = 'thot'


class ThotHandler(BaseHandler):

    @staticmethod
    @run_async
    @send_typing_action
    def __thot(bot: Bot, update: Update):
        """
        Thot.
        """
        update.message.reply_text(
            emojize(':peach:'))

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, ThotHandler.__thot)
