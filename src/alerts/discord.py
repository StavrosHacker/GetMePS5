import requests

from config import config
from utils import logger

config = config.read_config()
logger = logger.logger

def discordSend(msg):
    discord_webhook = config["discord_webhook"]
    mentions = config["discord_mentions"]
    new_mentions = ""
    for mention in range(0, len(mentions)):
        new_mentions = new_mentions + "<@"+mentions[mention]+">"
        
    try:
        response = requests.post(discord_webhook, data={"content": new_mentions + " " + msg})
    except:
        logger("Timed out while sending message via discord.", 0)