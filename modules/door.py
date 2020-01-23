def door(s):
	if '!door' in s and s[1] == 'in':
		return "I'm in!"
    if '!door' in s and len(s.split(' ')) > 1:
        return 'Let me in at '+s.split(' ')[1] + '!'
	if '!door' in s:
		return 'usage: !door <location>'

    return None
