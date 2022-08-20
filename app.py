from flask import Flask, Response
import os
import time

app = Flask(__name__)

@app.route('/ping')
def hello():
    return 'pong'

@app.route("/text_stream")
def text_stream():
    def generate():
        for n in range(61):
            yield f'{str(n)} sec<br>'
            time.sleep(1)

    return Response(generate())

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = os.environ.get('PORT'))
