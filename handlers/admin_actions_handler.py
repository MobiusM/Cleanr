from handlers import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CallbackQueryHandler
from consts import CLEANING_GROUP_ID

COMMAND_NAME = 'admin_actions'


class AdminActionHandler(BaseHandler):

    @staticmethod
    def __admin_actions(bot: Bot, update: Update):
        """
        Handle Admin options callbacks from private chat
        """
        query = update.callback_query
        if query.data == 'channel_announce':
            bot.send_message(CLEANING_GROUP_ID, 'Announcement test from admin!')

    @staticmethod
    def get_handler():
        return CallbackQueryHandler(AdminActionHandler.__admin_actions)
