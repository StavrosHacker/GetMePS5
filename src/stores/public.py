import requests

from utils import logger, alerts

logger = logger.logger
alerts = alerts.alerts

def publicSearch(ps5):
    site_domain = "public-cyprus.com.cy"
    ps5_name = "Disc Edition"
    ps5_buy = "https://www.public-cyprus.com.cy/product/"
    ps5_link = "https://www.public-cyprus.com.cy/cy/common/updateProductInfo.jsp?product="
    ps5_id = "prod10238545pp"

    if ps5 == "digital":
        ps5_name = "Digital Edition"
        ps5_id = "prod10810253pp"

    logger("Searching on " + site_domain + "..", 0)
    
    try:
        response = requests.get(ps5_link + ps5_id).json()
        status = response['productInfo'][0]['stockRule']
        if status != "εξαντλήθηκε!":
            msg = logger("PS5 " + ps5_name + " is in STOCK on " + site_domain + "\n\nBuy now -> " + ps5_buy + ps5_id + "/", 1)
            alerts(msg, 1)
        else:
            msg = "PS5 " + ps5_name + " is NOT in STOCK on " + site_domain + "\n"
    except:
        logger("Timed out while searching on " + site_domain + "\n", 0)