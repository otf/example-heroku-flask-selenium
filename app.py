from flask import Flask, Response
import os
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/poll")
def poll():
    def generate():
        yield '<ul>'
        i = 0
        while True:
            i += 1
            yield f'<li>{str(i)}</li>'
            time.sleep(1)

    return Response(generate())

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = os.environ.get('PORT'))
