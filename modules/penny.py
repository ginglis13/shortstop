import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def penny_pic_handler(sender, message, bot_id, app_id):
    with open('penny.txt') as f:
        images = []
        for line in f:
            images.append(line.strip())
        reply_image(images[random.randrange(len(images))], bot_id, app_id)
    return None
		

def reply_image(imgURL, bot_id, app_id):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
	    'bot_id': bot_id,
	    'text': "dank",
	    'picture_url' : imgURL
	}
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
