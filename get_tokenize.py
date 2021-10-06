import re
from datetime import datetime
import pandas as pd


def get_token_to_dataframe(file):
    with open(file, "r",encoding="utf-8") as f :
        chats = f.read().split("\n")

    data = []
    for chat in chats:
        try:
            time_logged = ",".join(chat.split("-")[0:3]).replace(",","-").strip()
            time_logged = datetime.strptime(time_logged,'%Y-%m-%d_%H:%M:%S')

            username_message = chat.split("-")[1:]
            username_message = '-'.join(username_message).strip()

            username,channel,message = re.search(
                ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)',username_message
            ).groups()

            d = {
                "dt":time_logged,
                "channel":channel,
                "username":username,
                "message":message
            }
            data.append(d)
        except Exception:
            pass

    return pd.DataFrame().from_records(data)

def get_tokenize(chat,id=None):
    time_logged = ",".join(chat.split("-")[0 :3]).replace(",", "-").strip()
    time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')
    username_message = chat.split("-")[1 :]
    username_message = '-'.join(username_message).strip()

    username, channel, message = re.search(
        ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
    ).groups()
    username = username.split("-")[1].strip()
    if id ==None:
        d = {
            "dt" : time_logged,
            "channel" : channel,
            "username" : username,
            "message" : message
        }
    else:
        d = {
            "_id":id,
            "dt" : time_logged,
            "channel" : channel,
            "username" : username,
            "message" : message
        }
    return d

