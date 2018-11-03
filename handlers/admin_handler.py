from handlers import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler
from utils import restricted, private_only

COMMAND_NAME = 'admin'


class AdminHandler(BaseHandler):

    @staticmethod
    @restricted
    @private_only
    def __admin(bot: Bot, update: Update):
        """
        Handle Admin options from private chat
        """
        update.message.reply_text("Hello Daddy")

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, AdminHandler.__admin)
