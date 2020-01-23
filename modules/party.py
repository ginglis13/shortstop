
def party(s):
    if '!party' in s:
        s = s.strip().split()
        if len(s) > 3:
            return "Imminent noise complaint at {} {}, {}".format(s[1], s[2], ' '.join(s[3:]))
        else:
            return "Usage: !party <building> <room> <time>"
    return None