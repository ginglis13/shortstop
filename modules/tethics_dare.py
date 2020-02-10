import json
import random
'''All dares subject to change '''
dares = []
dares[0:19]     = (20) * ["10 second chug"]
dares[20:24]    = (5)  * ["Show your feet"]
dares[25:34]    = (10) * ["Private message Ryan, \"what's up bro\""]
dares[35:44]    = (10) * ["Laptop barrel roll"]
dares[45:64]    = (20) * ["Take a lap around the room with your streaming device"]
dares[65:74]    = (10) * ["Put on a neighbor\'s coat or sweatshirt"]
dares[75:79]    = (5) * ["\"Accidentally\" raise your hand in Zoom"]
dares[80:84]    = (5) * ["Message the entire class on Zoom \"Hey <Person who dared you>\""]
dares[85:99]    = (15) * ["Hold your pencil/pen in your mouth for 30 seconds"]
dares[100:109]  = (10) * ["Ask a question and include the word \"avocado\""]
dares[110:124]  = (15) * ["Ask a question and reference the \"Bensalem Bytes\""]
dares[125:139]  = (15) * ["Complement the Wisdom of Salomon Podcast"]
dares[140:154]  = (15) * ["Defend the U-Chip"]
dares[155:159]  = (5) * ["Draw a picture and show the camera"]
dares[160:169]  = (10) * ["Disagree with the next topic"]
dares[170:184]  = (15) * ["Agree with the next topic"]
dares[185:194]  = (10) * ["Turn on your mic until being requested to mute"]
dares[195:204]  = (10) * ["\"Voluntold\" someone else in the class"]
dares[205:209]  = (5) * ["Reference the fact that Ryan and Bourgeious are both in South Bend"]
dares[210:214]  = (5) * ["Turn on your greenscreen, then ask a question"]
dares[215:224]  = (10) * ["Safe turn, but the next dare you give must be to a random person"]
dares[225:239]  = (15) * ["Close Zoom while making a comment"]

def dare_handler(sender, message, bot_id, app_id): 
    '''Dare a person in the class or randomly dare'''
    message = message.strip().split()
    if len(message) == 2:
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
    random.seed()
    roll = random.randint(0,len(dares))
    return dares[roll]
        


if __name__ == '__main__':
    print(dare_handler('Brennen Hogan','!tehics_dare dierre',' ',' '))