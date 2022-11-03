import base64
from io import BytesIO

from flask import Flask, request, render_template
from PIL import Image
import base64
import io

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import plot_2D

app = Flask(__name__)
class web_logger:
    def __init__(self):
        self.plots = []

    def reset(self):
        self.plots = []
        return '0'

    def render(self):
        img = []
        for p in self.plots:
            # img.append(plot.file_name + '.png')
            # temp_img = Image.frombytes('RGB', p.fig.canvas.get_width_height(),p.fig.canvas.tostring_rgb())
            temp_data = io.BytesIO()
            p.fig.savefig(temp_data, format='png')
            temp_data.seek(0)
            img.append('<img src="data:image/png;base64,{}" width="600" height="600">'.format(base64.b64encode(temp_data.getvalue()).decode('utf-8')))
        temp = img[0]
        for i in range(1,len(img)):
            temp += img[i]
        # return render_template('index.html', img_data = temp)
        return temp

    def add_plot(self, temp_dict):
        self.plots.append(plot_2D(temp_dict['x_label'], temp_dict['y_label'], temp_dict['title'], temp_dict['color'], temp_dict['file_name']))
        return '0'

    def plot(self, temp_dict):
        self.plots[temp_dict['index']].plot(temp_dict['x'], temp_dict['y'], color = temp_dict['color'], label = temp_dict['label'])
        return '0'
    
    def update_plot(self, temp_dict):
        self.plots[temp_dict['index']].update_plot(temp_dict['x'], temp_dict['y'], color = temp_dict['color'])
        return '0'

    def save(self):
        print(len(self.plots))
        for plot in self.plots:
            plot.save()
        return '0'

    def save_data(self):
        for plot in self.plots:
            plot.save_data()
        return '0'

    def clear(self):
        for plot in self.plots:
            plot.clear_plot()
        return '0'

    def clear_id(self, temp_dict):
        self.plots[temp_dict['index']].clear_plot()
        return '0'

    def update_title(self, temp_dict):
        self.plots[temp_dict['index']].update_title(temp_dict['title'])
        return '0'






wl = web_logger()

@app.route('/')
def __call_render():
    return wl.render()
@app.route('/add_plot', methods = ['POST'])
def __call_add_plot():
    temp_dict = request.get_json()
    return wl.add_plot(temp_dict)
@app.route('/plot', methods = ['POST'])
def __call_plot():
    temp_dict = request.get_json()
    return wl.plot(temp_dict)
@app.route('/update_plot', methods = ['POST'])
def __call_update_plot():
    temp_dict = request.get_json()
    return wl.update_plot(temp_dict)
@app.route('/save')
def __call_save():
    return wl.save()

@app.route('/save_data')
def __call_save_data():
    return wl.save_data()


@app.route('/index')
def __call_index():
    return render_template('index.html', template_folder = 'templates')

@app.route('/clear')
def __call_clear():
    return wl.clear()

@app.route('/reset')
def __call_reset():
    return wl.reset()

@app.route('/clear_id', methods = ['POST'])
def __call_clear_id():
    temp_dict = request.get_json()
    return wl.clear_id(temp_dict)

@app.route('/update_title', methods = ['POST'])
def __update_title():
    temp_dict = request.get_json()
    return wl.update_title(temp_dict)









if __name__ == '__main__':
    app.run(debug = True)





'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Image</title>
</head>
<body>
    <img id="picture" src="data:image/rgb;base64,{{ img_data }}">
</body>
</html>'''