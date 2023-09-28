import os

if not os.environ.get("TOKEN") or not os.environ.get("DATABASE_URL"):
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

from telegram.ext import Filters

BOT_TOKEN = os.environ.get("TOKEN")
DB_URI = os.environ.get("DATABASE_URL")
SUDO_USERS = [
    give sudo uers id
]
SUDO = Filters.user(SUDO_USERS)
LOG_CHAT = "Enter your chat id starting from minus, write without quotes"
