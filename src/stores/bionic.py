import requests

from utils import logger, alerts

logger = logger.logger
alerts = alerts.alerts

def bionicSearch(ps5):
    site_domain = "bionic.com.cy"
    ps5_name = "Disc Edition"
    ps5_link = "https://bionic.com.cy/products/sony-playstation-5-ps5-standard-edition"
    edition = 0

    if ps5 == "digital":
        ps5_name = "Digital Edition"
        ps5_link = "https://bionic.com.cy/products/sony-playstation-5-ps5-digital-edition"
        edition = 1

    logger("Searching on " + site_domain + "..", 0)

    headers = {
        'authority': 'bionic.com.cy',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-csrf-token': 'r7jmOEdZBwczk+F9Eb2otz45FqWdnb8wJKZJvvIilwrR9HM1R3Nav048b/aKngp518+dAG7bhTLcrIa3fPCN5g==',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'content-type': 'application/json',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://bionic.com.cy/products?keywords=playstation%205&order_by=price-desc',
        'accept-language': 'en,en-US;q=0.9',
        'cookie': 'cookieConsent=YES; cookieControl=true; bionic.com.cy_userRecentSearches=playstation%205; token=InNhamhOdUo5Ymo5Q21lR0YwQXRNS2cxNjEwOTcxMjMwOTI5Ig%3D%3D--00918f523da1b3276c06fb30f381f5ab74c9b6cd; guest_token=InNhamhOdUo5Ymo5Q21lR0YwQXRNS2cxNjEwOTcxMjMwOTI5Ig%3D%3D--00918f523da1b3276c06fb30f381f5ab74c9b6cd; _ga=GA1.3.697536984.1610971233; _fbp=fb.2.1613732645284.1110065421; __zlcmid=12jjp48qdkvmrLr; MCPopupClosed=yes; __cfduid=d50b727107b3c6b75bf62f6afad6b9c581616960694; _gid=GA1.3.1985086838.1616960698; cookieControl=true; cookieConsent=YES; bionic.com.cy_userRecentSearches=playstation%205%2C; _gat=1; _reactive_store_session=Ez48xY6XBqkDoTdHIIYAvihutplG%2BwSXWpsSa8z%2Fe7Y9mENB9DOnfjR2HlilIsA07g%2Fczu6f0hZ95ivOL39PyBe%2BmDBZdQ%2FD1qBcy0YRnU2%2Bemf%2Fb6jaH4jEsVetp%2Ft1GYufPS355HOS2mw758s%3D--VOEBByq8PKgINLK%2B--NjjRROtsKVLVSIadoqxNTg%3D%3D',
    }
    try:
        response = requests.get('https://bionic.com.cy/products?keywords=playstation%205&order_by=price-desc&_=1617044011124', headers=headers).json()
        status = response['products'][edition]['cart_status']['message']
        if status != "out_of_stock":
            msg = logger("PS5 " + ps5_name + " is in STOCK on " + site_domain + "\n\nBuy now -> " + ps5_link, 1)
            alerts(msg, 1)
        else:
            msg = "PS5 " + ps5_name + " is NOT in STOCK on " + site_domain + "\n"
    except:
        logger("Timed out while searching on " + site_domain + "\n", 0)