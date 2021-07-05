import requests

from config import config
from utils import logger

config = config.read_config()
logger = logger.logger

def slackSend(msg):
    slack_webhook = config["slack_webhook"]
    mentions = config["slack_mentions"]
    new_mentions = ""
    for mention in range(0, len(mentions)):
        new_mentions = new_mentions + "<@"+mentions[mention]+">"

    send = new_mentions + " " + msg
    payload = '{"text": "%s"}' % send
    try:
        response = requests.post(slack_webhook, data=payload)
    except:
        logger("Timed out while sending message via slack.", 0)