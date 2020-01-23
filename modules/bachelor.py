

def bachelor(s):
    if '!roseceremony' in s or '!bachelor' in s:
        with open("bachelor.txt") as f:
            candidates = []
            for line in f:
                line = line.strip()
                candidates.append(line)
            return ', '.join(candidates)
    return None