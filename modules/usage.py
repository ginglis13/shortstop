# usage.py

def usage_handler(sender, message, bot_id, app_id) -> str:
    '''Display usage message for commands to chat'''
    if '!usage' in message:
        with open("README.md") as f:
            commands = []
            for line in f:
                line = line.strip()
                if '!' in line:
                    commands.append(line)
        return '\n '.join(commands)
    return None