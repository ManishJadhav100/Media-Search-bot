import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'Media_search1'
USER_SESSION = 'User_Bot1'
API_ID = 3780861
API_HASH = 'f0da0ce1c62042ffc0f1904bda7baa76'
BOT_TOKEN = '5274443907:AAHgHcPGT3FvcjHnd0p4thWIi_3zSNed8fE'
USERBOT_STRING_SESSION = 'BQAEcu1f1gmzOnJ7J_WZe6SvDs2mIBdvWex9fp1mY-RNqngRqQFRtV9N7CQlDD-0i6bzgr9cdTQVe0im0hKEo4GA-8tjakWjslJxTQcPLa3ntnTQS39junOnKmuHgsw2vf9BFfqSD3xo1hoMUv2bLYmwZl-pvClTAPb7jLs9Iu-jCW3xrD-39cE_vsMTG3c9QWb64_9WfS-ldG-caEfNXM7BAgAW1r8ctb9rCpXH6B__OH2auQ3nsADRi8jgjoK0GIaeRLClnD0L_lMOs30_nkwRnTJJFBlLCSTgZD1Lm3P5xWIw-qO1wG5MZRt0cJzj6yxkZiFg9ZJCIjKBw1aA_UUGUx3U7QA'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [1394463981]
CHANNELS = [-1001490115011]
AUTH_USERS = [1394463981]
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = 'mongodb+srv://moviesearch:Manya007@cluster0.p2e1q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
DATABASE_NAME = 'moviedata'
COLLECTION_NAME = 'sample'

# Messages
default_start_msg = """
**Hi, I'm MJ Movie Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @MJFreeFlix to use this bot')
