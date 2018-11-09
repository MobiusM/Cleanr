from typing import List
import logging
from handlers.base_handler import BaseHandler
from telegram.ext import Updater


class Handlers:
    """
    Super class that governs all handles.
    """

    def __init__(self, updater: Updater,
                 command_handlers: List[BaseHandler] = None,
                 conversation_handlers: List[BaseHandler] = None):
        self.logger = logging.getLogger(__name__)
        self.updater = updater
        self.command_handlers = command_handlers
        self.conversation_handlers = conversation_handlers

    def start_handlers(self):
        """
        Start all the available handlers.
        """
        self.__init_conversation_handlers()
        self.__init_command_handlers()

    def __init_command_handlers(self) -> None:
        """
        Initialize all command handlers.
        """
        if self.command_handlers is not None:
            for handler in self.command_handlers:
                self.updater.dispatcher.add_handler(handler.get_handler())
        else:
            self.logger.warning('No command handlers are enabled.')

    def __init_conversation_handlers(self) -> None:
        """
        Initialize all conversation handlers.
        """
        if self.conversation_handlers is not None:
            for handler in self.conversation_handlers:
                self.updater.dispatcher.add_handler(handler.get_handler())
        else:
            self.logger.warning('No conversation handlers are enabled.')
