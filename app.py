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
    message = request.get_json()['text']
    print(message)

    noise_complaint(message)
    sign_in(message)
    detain(message)

    # TODO: bot logic

    return "ok", 200


def detain(msg):
    """Detain a user"""
    msg = msg.split()
    if msg[0].lower().startswith("!detain") and len(msg) < 4:
        reply(' '.join(msg[1:]) + " has been detained")


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


def noise_complaint(msg):
    if msg == msg.upper():
        reply("Noise complaint registered with room 202")


def sign_in(msg):
    if '!attendance' in msg:
        reply("https://docs.google.com/forms/u/0/d/e/1FAIpQLScYQDbMuOAH4EVpUlCAPxRhmPMJGXoYnR0Loo3fIrDzp6ZgTg/formResponse")


if __name__ == '__main__':
    app.run(host='167.172.204.173')
