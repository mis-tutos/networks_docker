from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    r = requests.get('http://app_dos_web_1:5000/')
    if r.status_code == 200:
        return 'hello world from app dos'
    else:
        return 'no conecto'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)