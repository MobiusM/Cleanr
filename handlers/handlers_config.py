from handlers.commands.thot_handler import ThotHandler
from handlers.commands.hello_handler import HelloHandler
from handlers.admin.admin_handler import AdminStartHandler
from handlers.admin.announce_handler import AdminAnnounceHandler
from handlers.admin.admin_conversation_router import AdminHandler

# Enabled command handlers (e.g. /hello)
COMMAND_HANDLERS = [HelloHandler, ThotHandler, AdminStartHandler, AdminAnnounceHandler]

# Enabled conversation handlers
CONVERSATION_HANDLERS = [AdminHandler]
