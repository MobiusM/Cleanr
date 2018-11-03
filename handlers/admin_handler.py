from handlers import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from utils import restricted, private_only, build_menu

COMMAND_NAME = 'admin'


class AdminHandler(BaseHandler):

    @staticmethod
    @restricted
    @private_only
    def __admin(bot: Bot, update: Update):
        """
        Handle Admin options from private chat
        """
        button_list = [
            InlineKeyboardButton("Announce", callback_data='channel_announce')
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        update.message.reply_text("Hello Daddy.\nChoose wisely!", reply_markup=reply_markup)

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, AdminHandler.__admin)
