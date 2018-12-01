from telegram import ReplyKeyboardMarkup
from telegram.bot import Bot
from telegram.ext import CommandHandler
from telegram.update import Update

from consts import CLEANING_GROUP_ID
from handlers.base_handler import BaseHandler
from utils import private_only, group_admin_only
from .admin_config import ADMIN_MENU_MARKUP, INPUT

COMMAND_NAME = 'admin'


class AdminHandler(BaseHandler):

    @staticmethod
    @private_only
    @group_admin_only(CLEANING_GROUP_ID)
    def __admin_start(bot: Bot, update: Update):
        """
        Admin menu entry point.
        """
        markup = ReplyKeyboardMarkup(ADMIN_MENU_MARKUP, one_time_keyboard=True)
        update.message.reply_text("This is the admin menu!\nChoose carefully.", reply_markup=markup)

        return INPUT

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, AdminHandler.__admin_start)
