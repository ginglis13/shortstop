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
from modules.daily_cal import daily_cal
from modules.door import door
from modules.usage import usage

app = Flask(__name__)

# get bot_id and api keys
with open(".secret", "r") as f:
    secrets = json.loads(f.read())
    bot_id = secrets['bot_id']
    OWN_APPID = secrets['weather']
    application_id = secrets['appid']

def call_handler(message):
    command = message.split()[0]
    methods = {
        '!attendance': sign_in,
        '!detain': detain,
        '!weather': weather_handler,
        '!party': party,
		'!door': door,
		'!usage', usage,
        '!dierre': dierre_pic_handler,
        '!roseceremony': bachelor,
        '!bachelor': bachelor,
        '!calendar': daily_cal
    }
    # Get the function from handlers dictionary, add message as argument, return None on KeyError
    handler = methods.get(command)

    # Execute the function
    if handler: return handler(message)
    return None

@app.route('/', methods=['POST'])
def shortstop():
    sender = request.get_json()['name']
    message = request.get_json()['text']
    
    # Log message
    print(message)

    # Bot logic
    if message and len(message) > 0 and message[0] == '!':
        # Get response from handler, if it's a valid command
        res = call_handler(message)
        if res: reply(res)
    # Check if noise complaint in order
    elif message == message.upper():
        reply(noise_complaint(message))

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
