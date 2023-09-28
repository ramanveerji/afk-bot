import os
from decouple import config

# Load variables from the .env file
BOT_TOKEN = config('TOKEN')
DB_URI = config('DATABASE_URL')
SUDO_USERS = config('SUDO_USERS').split(',')  # Split the comma-separated values into a list
LOG_CHAT = config('LOG_CHAT')

# Check if the required variables are defined
if not BOT_TOKEN or not DB_URI:
    print("Please specify TOKEN and DATABASE_URL environment variables in the .env file.")
    exit()

# Now, you can use these variables in your script as before
from telegram.ext import Filters

SUDO = Filters.user(SUDO_USERS)
