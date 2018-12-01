from telegram.ext import ConversationHandler

from handlers.admin.admin_handler import AdminHandler
from handlers.admin.announcement_handler import AdminAnnouncementHandler
from handlers.admin.input_handler import InputHandler
from handlers.base_handler import BaseHandler
from .admin_config import ANNOUNCE, INPUT

COMMAND_NAME = 'admin_menu'


class AdminHandler(BaseHandler):

    @staticmethod
    def __get_entry_points():
        return [
            AdminHandler.get_handler()
        ]

    @staticmethod
    def __get_states():
        return {
            ANNOUNCE: [AdminAnnouncementHandler.get_handler()],
            INPUT: [InputHandler.get_handler()]
        }

    @staticmethod
    def __get_fallbacks():
        return [AdminHandler.get_handler()]

    @staticmethod
    def get_handler():
        return ConversationHandler(entry_points=AdminHandler.__get_entry_points(),
                                   states=AdminHandler.__get_states(),
                                   fallbacks=AdminHandler.__get_fallbacks())
