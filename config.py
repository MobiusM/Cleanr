from handlers import *
from jobs import RepeatedHelloJob

# Enabled command handlers (e.g. /hello)
COMMAND_HANDLERS = [HelloHandler, ThotHandler, AdminHandler]

# Enabled repeating jobs
# REPEATING_JOBS = [RepeatedHelloJob]
REPEATING_JOBS = []

