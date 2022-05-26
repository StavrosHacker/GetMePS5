from bs4 import BeautifulSoup
import requests
import re

from utils import logger, alerts

logger = logger.logger
alerts = alerts.alerts

def electrolineSearch(ps5):
    site_domain = "electroline.com.cy"
    ps5_name = "Disc Edition"
    ps5_link = "https://www.electroline.com.cy/en/products/computing/gaming130/gaming-consoles13022/sony-playstation-5-disc-version-white/"

    if ps5 == "digital":
        ps5_name = "Digital Edition"
        ps5_link = "https://www.electroline.com.cy/en/products/computing/gaming130/gaming-consoles13022/sony-playstation-5-digital-version-white/"

    logger("Searching on " + site_domain + "..", 0)
    
    try:
        response = requests.get(ps5_link).text
        soup = BeautifulSoup(response, "html.parser")
        status = soup.body.findAll(text=re.compile("Not available in stores"))
        status2 = soup.body.findAll(text=re.compile("Not available online"))
        if not status or not status2:
            msg = logger("PS5 " + ps5_name + " is in STOCK on " + site_domain + "\n\nBuy now -> " + ps5_link, 1)
            alerts(msg, 1)
        else:
            msg = "PS5 " + ps5_name + " is NOT in STOCK on " + site_domain + "\n"
    except:
        logger("Timed out while searching on " + site_domain + "\n", 0)
