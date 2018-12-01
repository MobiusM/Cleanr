from telegram.ext import ConversationHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
import logging

from handlers.base_handler import BaseHandler
from utils import send_typing_action

COMMAND_NAME = 'cancel'


class CancelHandler(BaseHandler):

    @staticmethod
    @send_typing_action
    def __announce(bot, update):
        """
        Announce a message to your cleaning group.
        """
        update.message.reply_text('Cancelled', reply_markup=ReplyKeyboardRemove())
        user_data.clear()
        return ConversationHandler.END

    @staticmethod
    def get_handler():
        return MessageHandler(Filters.text, CancelHandler.__announce)
