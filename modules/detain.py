

def detain(msg):
    """Detain a user"""
    msg = msg.split()
    if msg[0].lower().startswith("!detain") and len(msg) < 4:
        return ' '.join(msg[1:]) + " has been detained."
    return None