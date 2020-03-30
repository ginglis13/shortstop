import random

def cohort_quote_handler(sender, message, bot_id, app_id):
    message = message.strip().split()
    if len(message) == 1:
        return rand_quote()
    elif len(message) > 2 and message[1] == 'add':
        return add_quote(' '.join(message[3:]))
    else:
        return "Get random cohort quote.\n usage: !quote\n"

def rand_quote():
    quotes = []
    with open('cohort_quotes.txt') as f:
        for line in f:
            quotes.append(line.strip())
    return quotes[random.randrange(len(quotes))]

def add_quote(quote):
    if '"' not in quote:
        quote = '"' + quote
        if '-' in quote:
            quotes = quote.split('-')
            quote = quotes[0]+'" - '+quotes[1]
        else:
            quote = quote+ '"'

    with open('cohort_quotes.txt','a') as f:
        f.write('\n'+quote)
    return quote + ' added'

if __name__ == '__main__':
    print(cohort_quote_handler('Dierre','!quote',' ',' '))
    print(cohort_quote_handler('Dierre','!quote add This is a new quote - Joe',' ',' '))
