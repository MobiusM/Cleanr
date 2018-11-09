from .admin_config import ANNOUNCE, INPUT
from handlers.base_handler import BaseHandler
from handlers.admin.admin_handler import AdminStartHandler
from handlers.admin.announce_handler import AdminAnnounceHandler
from handlers.admin.announce_input_handler import AdminInputHandler
from telegram.ext import ConversationHandler

COMMAND_NAME = 'admin_menu'


class AdminHandler(BaseHandler):

    @staticmethod
    def __get_entry_points():
        return [
            AdminStartHandler.get_handler()
        ]

    @staticmethod
    def __get_states():
        return {
            ANNOUNCE: [AdminAnnounceHandler.get_handler()],
            INPUT: [AdminInputHandler.get_handler()]
        }

    @staticmethod
    def __get_fallbacks():
        return [AdminStartHandler.get_handler()]

    @staticmethod
    def get_handler():
        return ConversationHandler(entry_points=AdminHandler.__get_entry_points(),
                                   states=AdminHandler.__get_states(),
                                   fallbacks=AdminHandler.__get_fallbacks())
