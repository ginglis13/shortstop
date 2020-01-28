#!/usr/bin/env python3
def door_handler(sender, message, bot_id, app_id) -> str:
    '''
    Get in the door wherever you at
    '''    
    usage_message = "Let me in the door!\nusage: !door <optional: location | in>"

    message = message.strip().split()

    if len(message) == 1:
        return "Let me in!"
    elif len(message) == 2:
        if message[1] == "in":
            return "I'm in!"
        else:
            return 'Let me in at ' + message[1] + '!'
    else:
        return usage_message
    return None

if __name__ == '__main__':
    print(door_handler("ben", "!door in", "x", "x"))
    print(door_handler("jack", "!door", "x", "x"))
    print(door_handler("ben", "!door hi hi hi", "x", "x"))
