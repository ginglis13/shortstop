#!/usr/bin/env python3
def bug_handler(sender, message, bot_id, app_id):
    '''
    Report a bug
    '''
    print(message)

if __name__ == '__main__':
    bug_handler("ben", "!bug", "blah", "blah")