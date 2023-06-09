#!/usr/bin/env python

from flask import Flask, Response, request
import os
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

@app.route('/pages/<int:page_number>')
def page(page_number):
    sleep(1)
    return f'''
        <p id='txt'>{page_number} page</p>
        <a id='btn-next' href='/pages/{page_number + 1}'>next page</a>
    '''

@app.route("/")
def index():
    def generate(url_root):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        with webdriver.Chrome(options = options) as driver:
            driver.get(f'{url_root}pages/1')
            elm = (lambda by,value:
                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((by, value))
                    ))

            for n in range(60 * 3):
                yield f'{elm(By.ID, "txt").text},{datetime.now().isoformat()}\n'
                elm(By.ID, 'btn-next').click()

    return Response(
            response = generate(request.url_root),
            mimetype = 'text/csv',
            headers = [('Content-Disposition', 'attachment; filename=pages.csv')])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = os.environ.get('PORT'))
