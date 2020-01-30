import requests
import json
import pprint
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os


def upload_image_to_groupme(imgURL, app_id):
	imgRequest = requests.get(imgURL, stream=True)
	filename = 'temp.png'
	postImage = None
	if imgRequest.status_code == 200:
		# Save Image
		with open(filename, 'wb') as image:
			for chunk in imgRequest:
				image.write(chunk)
		# Send Image
		headers = {'content-type': 'application/json'}
		url = 'https://image.groupme.com/pictures'
		files = {'file': open(filename, 'rb')}
		payload = {'access_token': app_id}
		r = requests.post(url, files=files, params=payload)
		imageurl = r.json()['payload']['url']
		os.remove(filename)
		return imageurl

def penny_pic_handler(sender, message, bot_id, app_id):
    with open('penny.txt') as f:
        images = []
        for line in f:
            images.append(line.strip())
        reply_image(images[random.randrange(len(images))], bot_id, app_id)
    return None
		

def reply_image(imgURL, bot_id, app_id):
    url = 'https://api.groupme.com/v3/bots/post'
    imgURL = upload_image_to_groupme(imgURL, app_id)
    #urlOnGroupMeService = upload_image_to_groupme(imgURL)
    data = {
	    'bot_id': bot_id,
	    'text': "dank",
	    'picture_url' : imgURL
	}
    # 'picture_url': imgURL
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
