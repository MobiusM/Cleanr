from telegram import KeyboardButton

# Routes that are supported.
ANNOUNCE, INPUT = range(2)

# ADMIN_MENU = [[KeyboardButton(text='Announce message')],
#               [KeyboardButton(text='Done')]]

# Available options available to the admin.
ADMIN_MENU_MARKUP = [[KeyboardButton(text='Announcement')]]
