#!/usr/bin/env python3
import os
import json
import requests
from importlib import reload # for loading in all modules
import re

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from modules.bachelor import bachelor_handler
from modules.daily_cal import daily_cal_handler
from modules.detain import detain_handler
from modules.dierre_pics import dierre_pic_handler
from modules.door import door_handler
from modules.noise_complaint import noise_complaint_handler
from modules.party import party_handler
from modules.sign_in import sign_in_handler
from modules.usage import usage_handler
from modules.weather import weather_handler
from modules.train import train_handler

# Globs
app = Flask(__name__)

# get bot_id and api keys
with open(".secret", "r") as f:
    secrets = json.loads(f.read())
    bot_id = secrets['bot_id']
    app_id = secrets['appid']


def call_handler(sender, message, bot_id, app_id):
    """Route commands to the correct module function"""
    command = message.split()[0]
    methods = {
        '!attendance': sign_in_handler,
        '!bachelor': bachelor_handler,
        '!calendar': daily_cal_handler,
        '!detain': detain_handler,
        '!dierre': dierre_pic_handler,
        '!door': door_handler,
        '!party': party_handler,
        '!roseceremony': bachelor_handler,
        '!usage': usage_handler,
        '!weather': weather_handler,
        '!train': train_handler
    }

    # Get the function from handlers dictionary, add message as argument, return None on KeyError
    handler = methods.get(command)

    # Execute the function
    if handler: return handler(sender, message, bot_id, app_id)
    return None


@app.route('/', methods=['POST'])
def shortstop():
    """Handle requests from GroupMe"""
    sender = request.get_json()['name']
    message = request.get_json()['text']

    # Log message
    print(message)

    # Bot logic
    if message and len(message) > 0 and message[0] == '!':
        # Get response from handler, if it's a valid command
        res = call_handler(sender, message, bot_id, app_id)
        if res: reply(res)
    # Check if noise complaint in order
    elif message and message == message.upper() and len(message) > 0 and re.search('[A-Z]', message):
        reply(noise_complaint_handler(sender, message, bot_id, app_id))

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
