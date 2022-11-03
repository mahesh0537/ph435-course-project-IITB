from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import time


class plot_2D:
    def __init__(self, x_label, y_label, title, color, file_name = None):
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.color = color
        self.fig = plt.figure(dpi = 500)
        self.ax = self.fig.add_subplot(111)
        if file_name != None:
            self.file_name = file_name
        else:
            self.file_name = 'temp'

    def plot(self, x, y, color = None, label = None):
        if color == None:
            color = self.color
        if label is not None:
            print(label)
            self.ax.scatter(x, y, color = color, label = label)
        else:
            self.ax.scatter(x, y, color = color)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        self.ax.set_title(self.title)
        self.ax.legend([label])
        self.ax.legend(loc = 'lower right')

    def update_plot(self, x, y, color = None):
        if color == None:
            color = self.color
        self.ax.scatter(x, y, color = color)

    def clear_plot(self):
        self.fig.clf()

    def close(self):
        self.fig.close()


    def save(self):
        self.fig.savefig(self.file_name + '.png')
        print('Saved plot to ' + self.file_name + '.png')

    def save_data(self):
        np.savetxt(self.file_name + '.txt', np.column_stack((self.x, self.y)), delimiter = ',')

    def update_title(self, title):
        self.title = title
        self.ax.set_title(self.title)
















if __name__ == '__main__':
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plot = plot_2D('x', 'y', 'sin(x)','black', 'sin')
    plot.plot(x, y)
    plot.update_plot(x, z)
    # plot.clear_plot()
    plot.update_plot(x, z)
    plot.save()
    plot.save_data()
    plot.show()
