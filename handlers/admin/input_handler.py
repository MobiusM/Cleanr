from telegram.ext import Filters
from telegram.ext import MessageHandler
import logging

from handlers.base_handler import BaseHandler
from .admin_config import ANNOUNCE

COMMAND_NAME = 'input'


class InputHandler(BaseHandler):

    @staticmethod
    def __input(bot, update):
        """
        Request input text from an admin.
        """
        logging.info(f'Inside {COMMAND_NAME}')
        update.message.reply_text('What would you like to tell?')

        return ANNOUNCE

    @staticmethod
    def get_handler():
        return MessageHandler(Filters.text, InputHandler.__input)
