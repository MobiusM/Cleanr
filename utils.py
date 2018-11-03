from functools import wraps
from telegram.chataction import ChatAction
from consts import ADMINS


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
