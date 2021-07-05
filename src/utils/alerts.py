from config import config
from alerts import telegram, slack, discord

config = config.read_config()
telegram = telegram.telegramSend
slack = slack.slackSend
discord = discord.discordSend

counter = 0

def alerts(msg, stock):
    global counter
    
    if stock == 1:
        counter = counter + 1

    if config["enable_telegram"] == "true": telegram(msg)
    if config["enable_slack"] == "true": slack(msg)
    if config["enable_discord"] == "true": discord(msg)