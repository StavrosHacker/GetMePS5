from bs4 import BeautifulSoup
import requests
import re

from utils import logger, alerts

logger = logger.logger
alerts = alerts.alerts

def melesoftSearch(ps5):
    site_domain = "melesoft.com"
    ps5_name = "Disc Edition"
    ps5_link = "http://www.melesoft.com/playstation-5-console"
    
    logger("Searching on " + site_domain + "..", 0)

    try:
        response = requests.get(ps5_link).text
        soup = BeautifulSoup(response, "html.parser")
        status = soup.body.findAll(text=re.compile("Δεν υπάρχει στο απόθεμα."))
        if not status:
            msg = logger("PS5 " + ps5_name + " is in STOCK on " + site_domain + "\n\nBuy now -> " + ps5_link, 1)
            alerts(msg, 1)
        else:
            msg = "PS5 " + ps5_name + " is NOT in STOCK on " + site_domain + "\n"
    except:
        logger("Timed out while searching on " + site_domain + "\n", 0)
