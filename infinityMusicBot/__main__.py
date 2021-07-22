import requests
from pyrogram import Client as Bot

from infinityMusicBot.config import API_HASH
from infinityMusicBot.config import API_ID
from infinityMusicBot.config import BG_IMAGE
from infinityMusicBot.config import BOT_TOKEN
from infinityMusicBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="infinityMusicBot.modules"),
)

bot.start()
run()
