def door(sender, message):
    if '!door' in message and message[1] == 'in':
        return "I'm in!"
    if '!door' in message and len(message.split(' ')) > 1:
        return 'Let me in at '+ message.split(' ')[1] + '!'
    return None
