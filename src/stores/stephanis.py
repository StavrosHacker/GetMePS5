import requests

from utils import logger, alerts

logger = logger.logger
alerts = alerts.alerts

def stephanisSearch(ps5):
    site_domain = "stephanis.com.cy"
    ps5_name = "Disc Edition"
    ps5_buy = "https://www.stephanis.com.cy/en/products/gaming/gaming-consoles/playstation"
    ps5_link = "https://www.stephanis.com.cy/en/products/product-load-add-to-cart-data?productIDs=83459%2C101400&_=1617027877878"
    
    logger("Searching on " + site_domain + "..", 0)

    try:
        response = requests.get(ps5_link).json()
        if len(response) > 2 or len(response) < 2:
            msg = logger("PS5 " + ps5_name + " is PROBABLY in STOCK on " + site_domain + "\n\nBuy now -> " + ps5_buy, 1)
            alerts(msg, 1)
        else:
            msg = "PS5 " + ps5_name + " is NOT in STOCK on " + site_domain + "\n"
    except:
        logger("Timed out while searching on " + site_domain + "\n", 0)