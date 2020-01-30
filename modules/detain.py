#detain History
#firstName lastName N
def detain(sender, message, bot_id, app_id):
    """Detain a user"""
    usage = "Detain a user.\n\
             usage: !detain <user>\n\
             Get Number of Detains\n\
             usage: !detain\n\
             See Detain History\n\
             usage: !detain list"

    message = message.strip().split()
    if len(message) > 1:
        if message.split(' ')[1] == 'list':
            return detainList()
        writeDetain(sender)
        return "{} has been detained.".format(' '.join(message[1:]))
    else:
        return "{} has been detained {} times".format(' '.join(message[1:],getN(sender))
    return None

def getN(user):
    with open('detainHistory.txt') as f:
		for line in f:
			line.split(' ')[:2] == user.split(' '):
                return line.split(' ')[2]
    return 0

def writeDetain(user):
	with open('detainHistory.txt') as f:
        history = []
		for line in f:
			history.append(line)
    
    #Can do this more pythonically. List comp?
    #L
    for i in range(len(history)):
        if user.split(' ')[:2] == history[i].split(' ')[:2]:
            history[i] = history[i][:-1] + int(history[i][-1]) + 1
            break
    else:
        history.append(user+' 1')

    with open('detainHistory.text',"w") as f:
        for line in history:
            f.write(line)

 def detainList():
    history = []
    with open('detainHistory.txt') as f:
        for line in f:
            history.append(line)
    return '\n '.join(history)





    

            