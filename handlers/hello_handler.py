from handlers import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler
from utils import send_typing_action

COMMAND_NAME = 'hello'


class HelloHandler(BaseHandler):

    @staticmethod
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
