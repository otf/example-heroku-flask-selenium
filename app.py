from flask import Flask, Response
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/ping')
def hello():
    return 'pong'

@app.route("/text_stream")
def text_stream():
    def generate():
        for n in range(61):
            yield f'{str(n)} sec<br>'
            sleep(1)

    return Response(generate())

@app.route("/")
def index():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome(options = options) as driver:
        driver.get('https://example-heroku-flask-selenium.herokuapp.com/ping')
        return driver.page_source

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = os.environ.get('PORT'))
