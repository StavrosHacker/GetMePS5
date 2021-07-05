# GetMePS5

After two weeks of using this bot I was able to get a PS5 Disc Edition from Public! So now I'm releasing it.

This bot will check 10 different popular store's websites in Cyprus every few seconds and will text you as often as you want (see below how) if no stock is found, or will text you immediately if any of the store's websites have the PS5 in stock with a link on where to buy. Both PS5 disc and digital editions are supported.

NOTE: This bot is made for websites in Cyprus only! You can modify the bot to support other websites as well, but this bot was primarily made for people living in Cyprus.

# Currently supported stores:

1. Public Cyprus (100% working)
2. Bionic (100% working)
3. Electroline (100% working)
4. Stephanis (No PS5 list is added, so the bot checks if the number of Playstation consoles increase or decrease and will text you if there's a change)
5. Sony Center Cyprus (100% working)
6. Fidelity Center (100% working)
7. Mavros Larnaca (100% working, wanted to check from their private API, but python requests doesn't want to work with the specific headers)
8. Musical Paradise (100% working)
9. Melesoft (100% working)
10. BuyAway (100% working)

# Currently supported alerters:

1. Telegram
2. Slack
3. Discord

# Configure bot

Open settings.yml to configure which PS5 you want the bot to search for and to enable/disable telegram, slack or discord. For telegram you need to create a bot, and set your bot token and chat id. For slack, you need to create an app and set it's webhook url as well as your profile id for the bot to tag you so you can get notified. For discord you need to create a webhook for the channel in your server, and set that url as well as your profile id for the same reason as above.

Change text_hours for how often you want the bot to alert you so you can know that it's running.
Don't change sleep_seconds unless you want the bot to check more or less often.

# Run bot

1. pip3 install -r requirements.txt
2. cd src
3. configure settings.yml
4. python3 main.py

If you want this bot to run 24/7, get a linux VPS, install screen on it, run the bot and you're done.

# Requirements

* requests
* pyyaml
* beautifulsoup4

Let's get that PS5!
