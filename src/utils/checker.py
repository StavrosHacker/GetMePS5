from config import config
from utils import logger

config = config.read_config()
logger = logger.logger

def checker():
    success = 1

    try:
        ps5 = config["ps5_edition"]
        enable_telegram = config["enable_telegram"]
        enable_slack = config["enable_slack"]
        enable_discord = config["enable_discord"]

        if ps5 != "disc" and ps5 != "digital":
            logger("Select which PS5 you want the bot to seach for.", 0)
            success = 0
        
        if enable_telegram != "true" and enable_telegram != "false":
            logger("Make sure to enable or disable telegram.", 0)
            success = 0
            
        if enable_slack != "true" and enable_slack != "false":
            logger("Make sure to enable or disable slack.", 0)
            success = 0

        if enable_discord != "true" and enable_discord != "false":
            logger("Make sure to enable or disable discord.", 0)
            success = 0

        if success == 0:
            exit()
        else:
            logger("Successfully configured.", 0)
    except:
        logger("Something went wrong.", 0)
        exit()