from handlers import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler
from utils import restricted

COMMAND_NAME = 'admin'


class AdminHandler(BaseHandler):

    @staticmethod
    @restricted
    def __admin(bot: Bot, update: Update):
        """
        Handle Admin options from private chat
        """
        if update.message.chat.type != 'group':
            update.message.reply_text("Hello Daddy")

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, AdminHandler.__admin)
