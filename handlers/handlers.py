from typing import List
from handlers import BaseHandler
from telegram.ext import Updater


class Handlers:
    """
    Super class that governs all handles.
    """

    def __init__(self, updater: Updater, command_handlers: List[BaseHandler] = None):
        self.updater = updater
        self.command_handlers = command_handlers

    def start_handlers(self):
        """
        Start all the available handlers.
        """
        self.__init_command_handlers()

    def __init_command_handlers(self) -> None:
        """
        Initialize all command handlers.
        """
        for handler in self.command_handlers:
            self.updater.dispatcher.add_handler(handler.get_handler())
