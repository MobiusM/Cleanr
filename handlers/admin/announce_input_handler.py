from handlers.base_handler import BaseHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from .admin_config import ANNOUNCE

COMMAND_NAME = 'admin_announce'


class AdminInputHandler(BaseHandler):

    @staticmethod
    def __announce(bot, update):
        """
        Request the announcement text from the admin.
        """
        update.message.reply_text('What would you like to announce today?')

        return ANNOUNCE

    @staticmethod
    def get_handler():
        return MessageHandler(Filters.all, AdminInputHandler.__announce)
