import json
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
        if message[1] == 'list':
            return detainList()
        writeDetain(message[1:])
        return "{} has been detained.".format(' '.join(message[1:]))
    else:
        return "{} has been detained {} times".format(sender,getN(sender))
    return None

def getN(user):
    user = ''.join(user)
    with open('detainHistory.json', 'r') as f:
        history = json.load(f)
    if user in history:
        return history[user]
    return 0

def writeDetain(user):
    user = ' '.join(user)
    with open('detainHistory.json', 'r') as f:
        history = json.load(f)

    if user in history:
        history[user] = int(history[user]) + 1
    else:
        history[user] = '1'

    with open('detainHistory.json', 'w') as f:
        json.dump(history, f)
    
    

def detainList():
    historyStr = []
    with open('detainHistory.json', 'r') as f:
        history = json.load(f)

    for name in history:
        historyStr.append(name+' '+str(history[name]))
    
    return '\n'.join(historyStr)


if __name__ == '__main__':
    print('Test detain')
    print(detain('Joseph Gripenstraw','!detain Dierre Upshaw',' ',' '))
    print(detain('Joseph Gripenstraw','!detain Dierre',' ',' '))

    print('Test self count')
    print(detain('Dierre Upshaw','!detain',' ',''))
    print ('Test list')
    print(detain('Joseph Gripenstraw','!detain list',' ',''))


    

            