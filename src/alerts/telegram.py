import requests

from config import config
from utils import logger

config = config.read_config()
logger = logger.logger

def telegramSend(msg):
    bot_token = config["telegram_token"]
    bot_chatID = config["telegram_chat_id"]
    try:
        response = requests.get("https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chatID + "&parse_mode=Markdown&text=" + msg)
    except:
        logger("Timed out while sending message via telegram.", 0)