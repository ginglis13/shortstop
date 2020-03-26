import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def dierre_pic_handler(sender, message, bot_id, app_id):
    with open('dierre_pics.txt') as f:
        images = []
        for line in f:
            images.append(line.strip())
        reply_image(images[random.randrange(len(images))], bot_id, app_id)
    return None


def dierre_quote():
	quotes = []
	with open('dierre_quotes.txt') as f:
		for line in f:
			quotes.append(line.strip())
	return quotes[random.randrange(len(quotes))]
		

def reply_image(imgURL, bot_id, app_id):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
	    'bot_id': bot_id,
	    'text': dierre_quote(),
	    'picture_url' : imgURL
	}
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
