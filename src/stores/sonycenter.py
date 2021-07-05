from bs4 import BeautifulSoup
import requests
import re

from utils import logger, alerts

logger = logger.logger
alerts = alerts.alerts

def sonyCenterCySearch(ps5):
    site_domain = "sonycentercy.com"
    ps5_name = "Disc Edition"
    ps5_link = "https://sonycentercy.com/playstation-5/2186-sony-playstation-5-0711719395003.html"

    if ps5 == "digital":
        ps5_name = "Digital Edition"
        ps5_link = "https://sonycentercy.com/playstation-5/2187-sony-playstation-5-digital-edition-0711719395102.html"
        
    logger("Searching on " + site_domain + "..", 0)

    try:
        response = requests.get(ps5_link).text
        soup = BeautifulSoup(response, "html.parser")
        status = soup.body.findAll(text=re.compile("Out-of-Stock"))
        if not status:
            msg = logger("PS5 " + ps5_name + " is in STOCK on " + site_domain + "\n\nBuy now -> " + ps5_link, 1)
            alerts(msg, 1)
        else:
            msg = "PS5 " + ps5_name + " is NOT in STOCK on " + site_domain + "\n"
    except:
        logger("Timed out while searching on " + site_domain + "\n", 0)