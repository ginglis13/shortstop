def party(message):
    '''
    party(message)
        message: !party <content>
        return:  Details for party
    '''
    # Usage
    usage_message = "usage: !party <building> <room> <time>"

    # Correct format ought to be <build> <room> <time>
    message_content = message.strip().split()[1:]

    if len(message_content) == 1 and message_content[0] == "help":
        return usage_message

    if len(message_content) == 3:
        return "Imminent noise complaint at {} {}, {}".format(message_content[0], message_content[1], message_content[2])
    else:
        return usage_message
    return None