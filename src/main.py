from datetime import datetime, timedelta
import time

from config import config
from utils import logger, alerts, checker

from stores import bionic, electroline, fidelitycenter, mavroslarnaca, melesoft, musicalparadise, public, sonycenter, stephanis, buyaway

config = config.read_config()
logger = logger.logger
counter = alerts.counter
alerts = alerts.alerts
checker = checker.checker

bionicSearch = bionic.bionicSearch
publicSearch = public.publicSearch
stephanisSearch = stephanis.stephanisSearch
sonyCenterCySearch = sonycenter.sonyCenterCySearch
fidelityCenterSearch = fidelitycenter.fidelityCenterSearch
mavrosLarnacaSearch = mavroslarnaca.mavrosLarnacaSearch
musicalParadiseSearch = musicalparadise.musicalParadiseSearch
buyAwaySearch = buyaway.buyAwaySearch
melesoftSearch = melesoft.melesoftSearch
electrolineSearch = electroline.electrolineSearch

def main():
    global counter

    checker()

    current_time = datetime.now()
    new_time = current_time + timedelta(minutes=1)
    ps5 = config["ps5_edition"]
    logger("Let's get the PS5 you deserve!", 0)
    logger("Configured for PS5 " + ps5 + " edition.\n", 0)
    while True:
        current_time = datetime.now()

        bionicSearch(ps5)
        publicSearch(ps5)
        stephanisSearch(ps5)
        sonyCenterCySearch(ps5)
        fidelityCenterSearch(ps5)
        mavrosLarnacaSearch(ps5)
        #musicalParadiseSearch(ps5)
        buyAwaySearch(ps5)
        melesoftSearch(ps5)
        electrolineSearch(ps5) #keep last
        
        if current_time >= new_time:
            text_hours = config["text_hours"]
            new_time = current_time + timedelta(hours=text_hours)
            if counter == 0:
                alerts(logger("PS5 is OUT OF STOCK everywhere.\n\nLast checked: " + current_time.strftime("%d/%m/%Y %H:%M:%S"), 1), 0)
            else:
                counter = 0

        seconds = config['sleep_seconds']
        logger("Waiting for " + str(seconds) + " seconds..\n", 0)
        time.sleep(seconds)
        logger("Continuing..\n", 0)

if __name__ == "__main__":
    main()