
def sign_in(msg):
    """Return attendance google form"""
    if '!attendance' in msg:
        return "https://docs.google.com/forms/u/0/d/e/1FAIpQLScYQDbMuOAH4EVpUlCAPxRhmPMJGXoYnR0Loo3fIrDzp6ZgTg/formResponse"
    return None