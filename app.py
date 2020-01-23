#!/usr/bin/env python3


import os
import json
import requests
from importlib import reload # for loading in all modules

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from modules.dierre_pics import dierre_pic_handler
from modules.detain import detain
from modules.noise_complaint import noise_complaint
from modules.sign_in import sign_in
from modules.party import party
from modules.bachelor import bachelor
from modules.weather import weather_handler

app = Flask(__name__)

# get bot_id and api keys
with open(".secret", "r") as f:
    secrets = json.loads(f.read())
    bot_id = secrets['bot_id']
    OWN_APPID = secrets['weather']
    application_id = secrets['appid']


@app.route('/', methods=['POST'])
def shortstop():
    sender = request.get_json()['name']
    message = request.get_json()['text']
    print(message)

    # bot logic
    if message and len(message) > 0:
        if noise_complaint(message): reply(noise_complaint(message))
        if sign_in(message): reply(sign_in(message))
        if detain(message): reply(detain(message))
        if weather_handler(message, OWN_APPID): reply(weather_handler(message,OWN_APPID))
        if party(message): reply(party(message))
        dierre_pic_handler(message, bot_id, application_id)
        if bachelor(message): reply(bachelor(message))

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
