def detain(sender, message, bot_id, app_id):
    """Detain a user"""
    usage = "Detain a user.\n\
             usage: !detain <user>"

    message = message.strip().split()
    if len(message) > 1:
        return "{} has been detained.".format(' '.join(message[1:]))
    else:
        return usage
    return None