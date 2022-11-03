import requests

IP = 'http://localhost:5000/'



class LOGGER:
    def __init__(self):
        self.id = -1

    def add_plot(self, xlabel, ylabel, title, color = 'black', filename = None):
        self.id += 1
        if filename is None:
            filename =  title
        data = {'x_label': xlabel, 'y_label': ylabel, 'title': title, 'color': color, 'file_name': filename}
        r = requests.post(IP + 'add_plot', json=data)

    def update_plot(self, x, y, id = None, color = 'black'):
        if id is None:
            id = self.id
        data = {'x': x.tolist(), 'y': y.tolist(), 'index': id, 'color': color}
        r = requests.post(IP + 'update_plot', json=data)

    def plot(self, x, y, color, label, id = None):
        if id is None:
            id = self.id
        data = {'x': x.tolist(), 'y': y.tolist(), 'color': color, 'label': label, 'index': id}
        r = requests.post(IP + 'plot', json=data)

    def clear(self, id = None):
        if id is None:
            id = self.id
        data = {'index': id}
        r = requests.post(IP + 'clear_id', json=data)
    
    def reset(self):
        r = requests.get(IP + 'reset')

    def update_title(self, title, id = None):
        if id is None:
            id = self.id
        data = {'index':id, 'title':title}
        r = requests.post(IP + 'update_title', json = data)