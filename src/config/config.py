import yaml
import os

from utils import logger

logger = logger.logger
config_file = "settings.yml"

def read_config():
    try:
        if os.path.exists(config_file):
            with open(config_file, "r") as stream:
                config = yaml.load(stream, Loader=yaml.FullLoader)
                return config
        else:
            logger("Config not found.", 0)
            exit()
    except:
        logger("Error when reading config.", 0)
        exit()