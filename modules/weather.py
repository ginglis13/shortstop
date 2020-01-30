import requests
import json


# Globs

ZIPCODE = {
    'redwood':  94062, # Redwood, CA
    'nd':   46556, # Notre Dame, IN
    'menlo': 94025, # Menlo, CA
    'att': 94301 # Palo Alto, CA
}

DEFAULT_ZIPCODE = 94025

with open(".secret", "r") as f:
    secrets = json.loads(f.read())
    OWM_APPID = secrets['weather']

 
def weather_handler(sender, message, bot_id, app_id):
    
    args = message.strip().split()
    if len(args) > 1:
        return weather(args[1], OWM_APPID)
    else:
        return weather(None, OWM_APPID)

      
def weather(location, OWM_APPID):
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
    return message
