import socket
import logging
import os
from emoji import demojize
from dotenv import load_dotenv
from datetime import datetime
from get_tokenize import get_tokenize
import pymongo

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

mongo_server = os.getenv("MONGO_SERVER")
mongo_port = int(os.getenv("MONGO_PORT"))

myclient = pymongo.MongoClient(f"mongodb://{mongo_server}:{mongo_port}/")
twitchdb = myclient["TwitchChatDB"]
twitchusers = twitchdb["TwitchUsers"]
# get token adress https://twitchapps.com/tmi/
#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s - %(message)s',
#                    datefmt='%Y-%m-%d_%H:%M:%S',
#                    handlers=[logging.FileHandler('chat.log',encoding='utf-8')])
with socket.socket() as sock:

    sock.settimeout(120)

    server = os.getenv('SERVER')
    port = int(os.getenv('PORT'))
    nickname = os.getenv('NICKNAME')
    token = os.getenv('TOKEN')
    channel = os.getenv('CHANNEL')

    sock.connect((server,port))


    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    while True:
        resp = sock.recv(2048).decode('utf-8')
        resp = str(datetime.now()).split(".")[0].replace(" ","_") + str(" - ") + resp
        if resp.startswith('PING'):
            sock.send("PONG\n".encode("utf-8"))

        elif len(resp) > 0:
            resp = demojize(resp)
            try:
                data = twitchusers.insert_one(get_tokenize(resp))
                print(data)
            except:
                pass

