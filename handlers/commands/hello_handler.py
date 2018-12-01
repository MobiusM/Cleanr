from telegram.bot import Bot
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.update import Update

from handlers.base_handler import BaseHandler
from utils import send_typing_action

COMMAND_NAME = 'hello'


class HelloHandler(BaseHandler):

    @staticmethod
    @run_async
    @send_typing_action
    def __hello(bot: Bot, update: Update):
        """
        Tell a user hello.
        """
        update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, HelloHandler.__hello)
