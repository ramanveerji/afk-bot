import os
from dotenv import load_dotenv
from telegram.ext import Filters

if not os.environ.get("TOKEN") or not os.environ.get("DATABASE_URL"):
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()
    
load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
DB_URI = os.getenv("DATABASE_URL")
SUDO_USERS = os.getenv("SUDO_USERS")
SUDO = Filters.user(SUDO_USERS)
LOG_CHAT = os.getenv("LOG_CHAT")
