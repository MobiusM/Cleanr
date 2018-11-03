import logging
from functools import wraps
from telegram.chataction import ChatAction
from consts import ADMINS

logger = logging.getLogger(__name__)


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(*args, **kwargs):
        bot, update = args
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        func(bot, update, **kwargs)

    return command_func


def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(bot, update, *args, **kwargs)

    return wrapped


def group_only(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        if update.message.chat.type == 'group':
            return func(bot, update, *args, **kwargs)
        logger.log(logging.ERROR, f"{update.message.text} can only be used in a group chat.")
        return

    return wrapped


def private_only(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        if update.message.chat.type == 'private':
            return func(bot, update, *args, **kwargs)
        logger.log(logging.ERROR, f"{update.message.text} can only be used in a private chat.")
        return

    return wrapped
