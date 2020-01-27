

def bachelor_handler(sender, message, bot_id, app_id):
    if '!roseceremony' in message or '!bachelor' in message:
        with open("bachelor.txt") as f:
            candidates = []
            for line in f:
                line = line.strip()
                candidates.append(line)
            return ', '.join(candidates)
    return None