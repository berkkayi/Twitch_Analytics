import socket
import logging
import os
from emoji import demojize

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log',encoding='utf-8')])
with socket.socket() as sock:

    sock.settimeout(120)

    server = os.getenv('SERVER')
    port = os.getenv('PORT')
    nickname = os.getenv('NICKNAME')
    token = os.getenv('TOKEN')
    channel = os.getenv('CHANNEL')

    sock.connect((server,port))


    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    while True:
        resp = sock.recv(2048).decode('utf-8')
        if resp.startswith('PING'):
            sock.send("PONG\n".encode("utf-8"))
        elif len(resp) > 0:
            logging.info(demojize(resp))