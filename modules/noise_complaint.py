import re

def noise_complaint(sender, message, bot_id, app_id):
    """If you're being too loud, register a noise complaint"""
    if message == message.upper() and len(message) > 0 and re.search('[A-Z]', message):
        return "Noise complaint registered with Redwood room 202"
    return None