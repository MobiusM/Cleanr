from handlers import BaseHandler
from telegram.ext import CommandHandler

COMMAND_NAME = 'hello'


class HelloHandler(BaseHandler):

    @staticmethod
    def __hello(bot, update):
        """
        Tell a user hello.
        :param bot:
        :type bot: telegram.bot.Bot
        :param update:
        :return:
        """
        update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))

    @staticmethod
    def get_handler():
        return CommandHandler(COMMAND_NAME, HelloHandler.__hello)
