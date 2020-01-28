#!/usr/bin/env python3

import requests
import json

def train_handler(sender, message, bot_id, app_id) -> str:
    usage = "usage: !train <trainsystem> <station>\n\
            \t<trainsystem> Caltrain: CT, Bart: BA\n\
            \t<station> Stop code for station"
    trainsystems = ['CT', 'BA']

    message = message.strip().split()[1:]

    if len(message) != 2:
        return usage

    with open("../.secret", 'r') as f:
        secrets = json.loads(f.read())
        token = secrets["train_token"]
    
    agency = message[0]
    stopCode = message[1]

    URL = "http://api.511.org/transit/stoptimetable?api_key={}&OperatorRef={}&MonitoringRef=13008".format(token, agency, stopCode)

    print(URL)

    # r = requests.get(http://api.511.org/transit/StopMonitoring?api_key={your-key}&agency=)
    
    return None

if __name__ == '__main__':
    train_handler("!train BA 23")

