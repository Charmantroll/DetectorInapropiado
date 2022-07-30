from turtle import st
import requests
import json
	
def detect(api_key, img, link, output):
	if api_key != "":
		if img != "" and link == False:
			r = requests.post(
				"https://api.deepai.org/api/nsfw-detector",
    		files={
     		   'image': open(img, 'rb'),
  		  },
   		 headers={'api-key': api_key}
			)
			if output == True:
				return r.json()
			else:
				return ""
		
		if link != "" and img == False:
			r = requests.post(
				"https://api.deepai.org/api/nsfw-detector",
    		data={
        		'image': link,
  		  },
   		 headers={'api-key': api_key}
			)
			
			if output == True:
				return r.json()
			else:
				return ""
	if api_key == "":
			return "API Key is empty."
				
api_key = "921aeb62-8a72-4c38-b483-8eaa78be2900"

#print(detect(api_key, False, "https://raw.githubusercontent.com/MoleTheDev/DeepAI-Nudity-Detection/main/image.jpg", True))

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
	return json.dumps(detect(api_key, "", "", True))

@app.route('/api/<path:path>')
def catch_all(path):
	return json.dumps(detect(api_key, False, path, True))

if __name__ == '__main__':
	app.run(debug=True)