echo "Cloning Repo...."
git clone https://github.com/ramanveerji/afk-bot /afkbot
cd /afkbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py