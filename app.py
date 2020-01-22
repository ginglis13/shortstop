#!/usr/bin/env python3


import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)

# get bot_id
bot_id = ""
with open(".secret", "r") as f:
    bot_id = f.readlines()[0].strip()


@app.route('/', methods=['POST'])
def shortstop():
    print("hi")
    message = request.get_json()
    print(message)

    # TODO: bot logic 

    return "ok", 200


def reply(msg):
    """Reply to a message in the chat"""
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id'		: bot_id,
        'text'			: msg
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


def sender_is_bot(message):
    """Check if sender is bot to not reply to own msgs"""
    return message['sender_type'] == "bot"


if __name__ == '__main__':
    app.run(host='167.172.204.173')
