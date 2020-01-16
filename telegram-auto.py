import time
import requests
import schedule
from config import *

def telegram_bot_sendtext(chat_id ,bot_message, type):
    if type == "photo":
        send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendPhoto?chat_id=' + chat_id + '&parse_mode=Markdown&photo=' + bot_message
    if type == "text":
        send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chat_id + '&text=' + bot_message
    if type == "post":
        send_text = 'https://api.telegram.org/bot' + TOKEN + '/forwardMessage?chat_id=' + chat_id + bot_message

    response = requests.get(send_text)

    print("Sending... " + send_text)
    return response.json()

for info in ALL_INFO:
    chat_id = info["chat_id"]
    msg = info["msg"]
    type = info["type"]
    time_to_wait = info["time_to_wait"]
    schedule.every(time_to_wait).minutes.do(telegram_bot_sendtext, chat_id=chat_id, bot_message=msg, type=type)

while True:
    schedule.run_pending()
    time.sleep(1)