import flask
from flask import request, jsonify
from control import *

c = device()


app = flask.Flask(__name__)

@app.route('/setup_led', methods=['POST', 'GET'])
def setup_device():
    print('setup_device')
    data = request.args
    print(data["IP"])
    c.connect_light(data["IP"])
    c.light.set_brightness(5)
    c.light()
    status = c.light.get_status()
    print('status = ',status)
    c()

    return '0'

@app.route('/maximum', methods=['POST', 'GET'])
def maximum():
    print('maximum')
    c.light.set_brightness(15)
    c.light()
    status = c.light.get_status()
    print('status = ',status)
    c()

    return '0'

@app.route('/minimum', methods=['POST', 'GET'])
def minimum():
    print('minimum')
    c.light.set_brightness(1)
    c.light()
    status = c.light.get_status()
    print('status = ',status)
    c()

    return '0'

@app.route('/off', methods=['POST', 'GET'])
def off():
    print('off')
    c.light.turn_off()
    c.light()
    status = c.light.get_status()
    print('status = ',status)

    return '0'

@app.route('/medium', methods=['POST', 'GET'])
def medium():
    print('medium')
    c.light.set_brightness(8)
    c.light()
    status = c.light.get_status()
    print('status = ',status)

    return '0'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
