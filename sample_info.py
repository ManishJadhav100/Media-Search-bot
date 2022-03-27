# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = '1BVtsOI8Bu34VmZy5DmgYOzkSJa0LPHMKlv6NHeYkON6KIEUimJ-G6rJEDctvgdtCnut-lVRr1r7NPyDb2C7s-It6AnWZbaRb6tmrG5wpM0tp17VdvqMe0RCTH5VkOgnuibt-8Ci43YEBbC-0jsWNZxbt1exQMUJapSNP0KvsrgH3-Wt8y1YEf22QJm6UM_EBMWm6-rrWyPbW7sILLe6k8hRc-sLSp8O0qqEAX8S1FFUcFWCa1WvI5hbBbo9RtvyGcvuSUbvHMZBkHZvtig3ZewewmQbtcxeYmUwpCYSanS80500eW0V4b532gmQ0z790yeU7hiS5smkX4JwKnHrFWO4G3tp4XDY='

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
START_MSG = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press follwing buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = 'Please join @.... to use this bot'
