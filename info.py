import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'InfinityMoviesBot')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BOT_USERNAME = os.environ.get("BOT_USERNAME")

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#for broadcast and force sub
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)

#ban/unban
BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))


# Messages
default_start_massege = """
**Hi, I'm INFINITY Film Search bot.
හායි 😌 මම ෆිල්ම් හොයල දෙන බොට් කෙනෙක් ❤️**
__Here you can search files in inline mode. Just press following buttons and start searching.__
__ඔයාලට ඔනේ දෙවල් ලබාගන්න පහත ඉන්ලයින් බටන් එක යුස් කරන්න ❤️__
__📌 යට තියෙන බටන් එක ටච් කරල ඔයාට ඕනෙ **ෆිල්ම් එකේ නම හරියම අවුරැද්දත් එක්ක** ගහන්න__
**▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
       🔰🅸🅽🅵🅸🅽🅸🆃🆈 🅻🅺🔰
    ɪɴғɪɴɪᴛʏ_ʙᴏᴛs | @BOTS_Infinity  
          ᴏᴡɴᴇʀ 🔰 | 🔰 @Dx_Doc 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬**
"""

SHARE_BUTTON_TEXT = """
Infinity Media Search Bot

Here you can find any media file by searching its name 😊

Bot : {username} 🤖
Updates Channel: @BOTS_Infinity
"""

START_MSG = environ.get('START_MSG', default_start_massege)

INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
