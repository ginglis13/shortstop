import requests
import json
import pprint
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os


def upload_image_to_groupme(imgURL):
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
		payload = {'access_token': 'dlP5RZ20apdbNaGh2aHX6nVc40VSZsGLVNdNRfqL'}
		r = requests.post(url, files=files, params=payload)
		imageurl = r.json()['payload']['url']
		os.remove(filename)
		return imageurl

def dierre_pic_handler(s):
    if '!dierre' in s:
        with open('dierre_pics.txt') as f:
            images = []
            for line in f:
                images.append(line.strip())
            reply_image(images[random.randrange(len(images))])

def reply_image(imgURL):
    url = 'https://api.groupme.com/v3/bots/post'
    imgURL = upload_image_to_groupme(imgURL)
    #urlOnGroupMeService = upload_image_to_groupme(imgURL)
    data = {
	    'bot_id': 'a5a4f11434e289b8c042675339',
	    'text': '',
	    'picture_url' : imgURL
	}
    # 'picture_url': imgURL
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()