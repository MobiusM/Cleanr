from handlers import BaseHandler
from telegram.ext import CommandHandler
from emoji import emojize

COMMAND_NAME = 'thot'


class ThotHandler(BaseHandler):

    @staticmethod
    def __thot(bot, update):
        """
        Thot-ing around.
        :param bot:
        :type bot: telegram.bot.Bot
        :param update:
        :return:
        """
        update.message.reply_text(
            emojize(':eggplant::peach:'))

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, ThotHandler.__thot)
