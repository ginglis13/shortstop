#!/usr/bin/env python3


import os
import json
import requests
from importlib import reload # for loading in all modules

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from modules.dierre_pics import dierre_pic_handler

app = Flask(__name__)

ZIPCODE = {
    'redwood':  94062, # Redwood, CA
    'nd':   46556, # Notre Dame, IN
    'menlo': 94025, # Menlo, CA 
    'att': 94301 # Palo Alto, CA
}

DEFAULT_ZIPCODE = 94025


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
        weather_handler(message)
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


def detain(msg):
    """Detain a user"""
    msg = msg.split()
    if msg[0].lower().startswith("!detain") and len(msg) < 4:
        return ' '.join(msg[1:]) + " has been detained."
    return None


def noise_complaint(msg):
    """If you're being too loud, register a noise complaint"""
    if msg == msg.upper():
        return "Noise complaint registered with Redwood room 202"
    return none


def sign_in(msg):
    """Return attendance google form"""
    if '!attendance' in msg:
        return "https://docs.google.com/forms/u/0/d/e/1FAIpQLScYQDbMuOAH4EVpUlCAPxRhmPMJGXoYnR0Loo3fIrDzp6ZgTg/formResponse"
    return None

def party(s):
    if '!party' in s:
        s = s.strip().split()
        if len(s) > 3:
            return "Imminent noise complaint at {} {}, {}".format(s[1], s[2], ' '.join(s[3:]))
        else:
            return "Usage: !party <building> <room> <time>"
    return None

def bachelor(s):
    if '!roseceremony' in s or '!bachelor' in s:
        with open("bachelor.txt") as f:
            candidates = []
            for line in f:
                line = line.strip()
                candidates.append(line)
            return ', '.join(candidates)
    return None

def weather_handler(s):
    if '!weather' in s:
        args = s.strip().split()
        if len(args) > 1:
            weather(args[1])
        else:
            weather()

def weather(location=None):
    print('location', location)
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?zip={},us'

    if not location:
        location = DEFAULT_ZIPCODE 
    elif location in ZIPCODE:
        location = ZIPCODE[location]
    else:
        location = DEFAULT_ZIPCODE

    weather_url = weather_url.format(location)
    
    parm  = {
        'appid': OWM_APPID,
        'units': 'imperial',
    }

    resp = requests.get(weather_url, params=parm)
    resp = json.loads(resp.text)
    temp = resp['main']['temp']

    try:
        desc = resp['weather'][0]['description']
    except:
        desc = None

    message = 'Current weather in {} is {}°F, {}'.format(resp['name'], temp, desc)
    reply(message)

if __name__ == '__main__':
    app.run(host='167.172.204.173')
