from telegram.ext import ConversationHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
import logging

from handlers.base_handler import BaseHandler
from utils import send_typing_action

COMMAND_NAME = 'admin_announcement'


class AdminAnnouncementHandler(BaseHandler):

    @staticmethod
    @send_typing_action
    def __announce(bot, update):
        """
        Announce a message to your cleaning group.
        """
        logging.info(f'Inside {COMMAND_NAME}')
        announcement_text = update.message.text
        update.message.reply_text(
            f'You have sent the following text:\n\n'
            f'{announcement_text}')

        # bot.send_message(CLEANING_GROUP_ID, announcement_text)

        return ConversationHandler.END

    @staticmethod
    def get_handler():
        return MessageHandler(Filters.text, AdminAnnouncementHandler.__announce)
