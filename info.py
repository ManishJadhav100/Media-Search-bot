import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 3780861
API_HASH = 'f0da0ce1c62042ffc0f1904bda7baa76'
BOT_TOKEN = '5274443907:AAHgHcPGT3FvcjHnd0p4thWIi_3zSNed8fE'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [1394463981]
CHANNELS = [-1001490115011]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = 'mongodb+srv://moviesearch:Manya@004@cluster0.p2e1q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
DATABASE_NAME = 'movies'
COLLECTION_NAME = 'movies'

# Messages
default_start_msg = """
**Hi, I'm MJ Movie Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @MJFreeFlix to use this bot')
