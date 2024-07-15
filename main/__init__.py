#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22439323
API_HASH = "e0e203c8be2c2c58b04d0c59fc82f507"
BOT_TOKEN = "7470597083:AAFgqPndTMvlAOvPY8eoOpPqUXGRPWOxM80"
SESSION = "BQFxJpUAPvr-a9n-wtiSfmuOOTswU0IqcCuwjDMuaNzmGtY0c5-PPsE_FWT7Qu9HrKzdp7RKvGhPyNnCdPV17vhNeXEPAUN7c3Z4zHovujoGKR9NtRE1fXxq9wNIxL8Su6dknrYGlNAHtFfmiDBOGYkbBRb82DlBfUHHWqoot4ft5s4Ij5tVYejHKDTYgn7QqoQkBEG0MRzavygqNSX9cFsrfWN-6R8NGSdvDWJebjWRgPkMzfY1oPFiBaVN30rtlUf_p9uagC6uryjjNjk48_sdtj8ZViYySdVfQq4w-L5ORZkPIStiqMx7Q1UdMuG0jtjfRg-5s8nSMIKWDx7lV108BbCMbQAAAAG01izdAA"
FORCESUB = "neetumamvol_2"
AUTH = 7170416848

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
