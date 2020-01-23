def usage(s):
    if '!usage' in s:
        with open("README.md") as f:
            commands = []
            for line in f:
                line = line.strip()
                if '!' in line:
                    commands.append(line)
            return ', '.join(candidates)
    return None
