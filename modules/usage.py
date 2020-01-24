# usage.py

def usage(s):
    '''Display usage message for commands to chat'''
    if '!usage' in s:
        with open("README.md") as f:
            commands = []
            for line in f:
                line = line.strip()
                if '!' in line:
                    commands.append(line)
        return '\n '.join(commands)
    return None