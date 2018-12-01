from handlers.admin.admin_conversation_router import AdminHandler
from handlers.commands.hello_handler import HelloHandler
from handlers.commands.thot_handler import ThotHandler

# Enabled command handlers (e.g. /hello)
COMMAND_HANDLERS = [HelloHandler, ThotHandler]

# Enabled conversation handlers
CONVERSATION_HANDLERS = [AdminHandler]
