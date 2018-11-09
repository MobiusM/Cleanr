from telegram import ReplyKeyboardMarkup
from handlers.base_handler import BaseHandler
from .admin_config import ADMIN_MENU_MARKUP, INPUT
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler

from utils import private_only

COMMAND_NAME = 'admin'


class AdminStartHandler(BaseHandler):

    @staticmethod
    @private_only
    def __admin_start(bot: Bot, update: Update):
        """
        Admin menu entry point.
        """
        markup = ReplyKeyboardMarkup(ADMIN_MENU_MARKUP, one_time_keyboard=True)
        update.message.reply_text("This is the admin menu!\nChoose carefully.", reply_markup=markup)

        return INPUT

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, AdminStartHandler.__admin_start)
