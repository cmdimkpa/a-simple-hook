# A Hook Example

from flask import Flask

app = Flask(__name__)

global trigger

port = 2222
trigger = 0

@app.route('/request')
def req():
    global trigger
    while trigger == 0:
        pass
    trigger = 0
    return "response"

@app.route('/fire')
def fire():
    global trigger
    trigger = 1
    return "fired"

if __name__ == "__main__":
    app.run(host="localhost",port=port)
