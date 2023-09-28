import os
from dotenv import load_dotenv
from telegram.ext import Filters

# Load environment variables from a .env file (if present)
load_dotenv()

# Retrieve values from environment variables
BOT_TOKEN = os.getenv("TOKEN")
DB_URI = os.getenv("DATABASE_URL")
SUDO_USERS = os.getenv("SUDO_USERS")

# Check if the required environment variables are set
if not BOT_TOKEN or not DB_URI:
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

# Convert SUDO_USERS into a list of user IDs
SUDO_USER_IDS = [int(user_id) for user_id in (SUDO_USERS.split(',') if SUDO_USERS else [])]

# Create a Filters.user() filter based on SUDO_USER_IDS
SUDO = Filters.user(SUDO_USER_IDS)
LOG_CHAT = os.getenv("LOG_CHAT")

# Your bot code can continue from here...
