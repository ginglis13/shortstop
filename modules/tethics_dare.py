
import json
import random

def dare_handler(sender, message, bot_id, app_id):
    '''Dare a person in the class or randomly dare'''
    message = message.strip().split()
    if len(message) is 2:
        dare = tehics_dares()
        if message[1].lower() == "random":
            message[1] = random_classmate()
        return "{} has been dared by {} to:\n{}\nTime to earn those participation points".format(message[1], sender, dare)
    else:
        return "Issue a tethics dare.\n usage: !dare <user>\n"

def random_classmate():
    roster = []
    with open('tethics_roster.txt') as f:
        for line in f:
            roster.append(line.strip())
    return roster[random.randrange(len(roster))]

def tehics_dares():
    dares = []
    with open('dares.txt') as f:
        for line in f:
            dares.append(line.strip())
    return dares[random.randrange(len(dares))]
        


if __name__ == '__main__':
    print(dare_handler('Brennen Hogan','!tehics_dare Random',' ',' '))
