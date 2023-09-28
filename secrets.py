import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if present)
load_dotenv()

# Retrieve values from environment variables
BOT_TOKEN = os.getenv("TOKEN")
DB_URI = os.getenv("DATABASE_URL")

# Check if the required environment variables are set
if not BOT_TOKEN or not DB_URI:
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

LOG_CHAT = os.getenv("LOG_CHAT")

# Your bot code can continue from here...
