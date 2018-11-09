from handlers.base_handler import BaseHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import ConversationHandler
from consts import CLEANING_GROUP_ID

COMMAND_NAME = 'admin_announce'


class AdminAnnounceHandler(BaseHandler):

    @staticmethod
    def __announce(bot, update):
        """
        Announce a message to your cleaning group.
        """
        announcement_text = update.message.text
        update.message.reply_text(
            f'You have sent the following text:\n\n'
            f'{announcement_text}')

        # todo: add confirmation stage before sending. If yes is supplied, send to group, if no, offer to edit message.
        # todo: if a message was sent that has a mistake in it, add a command to edit the last announcement. Find a way to store last announcement.

        bot.send_message(CLEANING_GROUP_ID, announcement_text)

        return ConversationHandler.END

    @staticmethod
    def get_handler():
        return MessageHandler(Filters.all, AdminAnnounceHandler.__announce)
