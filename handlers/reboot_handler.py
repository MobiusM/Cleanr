import os

from handlers import BaseHandler
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import CommandHandler
from utils import restricted, private_only

COMMAND_NAME = 'reboot'


class RebootHandler(BaseHandler):

    @staticmethod
    @restricted
    @private_only
    def __reboot(bot: Bot, update: Update):
        """
        Reboot:
        stops bot, pulls from git master, and restarts.
        """
        update.message.reply_text("Rebooting bot!")
        os.execl('reboot.sh', 'reboot.sh')

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, RebootHandler.__reboot)

