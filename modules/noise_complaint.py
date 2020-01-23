

def noise_complaint(msg):
    """If you're being too loud, register a noise complaint"""
    if msg == msg.upper():
        return "Noise complaint registered with Redwood room 202"
    return None