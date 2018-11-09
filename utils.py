import logging
from functools import wraps
from mwt import mwt
from telegram.chataction import ChatAction

logger = logging.getLogger(__name__)


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(*args, **kwargs):
        bot, update = args
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        func(bot, update, **kwargs)

    return command_func


def group_only(func):
    """
    Use callback function only in a group.
    """

    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        if update.message.chat.type == 'group':
            return func(bot, update, *args, **kwargs)
        logger.error(f"{update.message.text} can only be used in a group chat.")
        return

    return wrapped


def private_only(func):
    """
    Use callback function only in a private chat.
    """

    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        if update.message.chat.type == 'private':
            return func(bot, update, *args, **kwargs)
        logger.error(f"{update.message.text} can only be used in a private chat.")
        return

    return wrapped


@mwt(timeout=60 * 60)
def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
