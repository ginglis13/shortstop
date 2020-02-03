
import json
import random

def dare_handler(sender, message, bot_id, app_id):
    """Detain a user"""
    message = message.strip().split()
    if len(message) is 2:
        dare = tehics_dares()
        #dare = 'drink piss'
        return "{} has been dared by {} to:\n{}\nTime to earn those participation points".format(message[1], sender, dare)
    else:
        return "Issue a tethics dare.\n usage: !dare <user>\n"


def tehics_dares():
	dares = []
	#with open('/Users/brennen/School/Junior Year/shortstop/dares.txt') as f:
    with open('dares.txt') as f:
		for line in f:
			dares.append(line.strip())
	return dares[random.randrange(len(dares))]
		


if __name__ == '__main__':
    print('Test dare')
    print(dare_handler('Brennen Hogan','!tehics_dare Dierre',' ',' '))