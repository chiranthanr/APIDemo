import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    result = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    for data in result.json()['items']:
       print(data['title'])
    return 'This is the output from the API'
