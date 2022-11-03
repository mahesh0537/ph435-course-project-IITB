from flask import Flask, request, jsonify
from time import sleep
from logger import LOGGER
import numpy as np

import requests
app = Flask(__name__)

l = LOGGER()
l.reset()
@app.route('/add_plot', methods=['POST', 'GET'])
def add_plot():
    IP = 'http://'+request.args['IP']
    print(IP)
    l.add_plot('time_scale', 'amplitude', 'test')
    t = 0
    while True:
        r = requests.get(IP + '/status')
        r = r.text
        r = r.split(' ')
        print(r)
        r = int(r[-1])
        l.update_plot(np.array([t]), np.array([float(r)]))
        t += 1
        sleep(5)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)