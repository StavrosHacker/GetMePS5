import requests

from utils import logger, alerts

logger = logger.logger
alerts = alerts.alerts

def publicSearch(ps5):
    site_domain = "public.cy"
    ps5_name = "Disc Edition"
    ps5_buy = "https://www.public.cy/product/gaming/consoles/ps5/"
    ps5_link = "https://www.public.cy/public/v2/sku/"
    ps5_id = "1428499"

    if ps5 == "digital":
        ps5_name = "Digital Edition"
        ps5_id = "1530295"

    logger("Searching on " + site_domain + "..", 0)
    
    try:
        response = requests.get(ps5_link + ps5_id).json()
        status = response['sku']['miraklHasStock']
        if status != "false":
            msg = logger("PS5 " + ps5_name + " is in STOCK on " + site_domain + "\n\nBuy now -> " + ps5_buy + ps5_id + "/", 1)
            alerts(msg, 1)
        else:
            msg = "PS5 " + ps5_name + " is NOT in STOCK on " + site_domain + "\n"
    except:
        logger("Timed out while searching on " + site_domain + "\n", 0)
