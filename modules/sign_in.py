
def sign_in(sender, message, bot_id, app_id):
    """Return attendance google form"""
    if '!attendance' in message:
        return "https://docs.google.com/forms/u/0/d/e/1FAIpQLScYQDbMuOAH4EVpUlCAPxRhmPMJGXoYnR0Loo3fIrDzp6ZgTg/formResponse"
    return None