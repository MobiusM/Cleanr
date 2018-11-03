from handlers import HelloHandler, ThotHandler
from jobs import RepeatedHelloJob

# Enabled command handlers (e.g. /hello)
COMMAND_HANDLERS = [HelloHandler, ThotHandler]

# Enabled repeating jobs
REPEATING_JOBS = [RepeatedHelloJob]
