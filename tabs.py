import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PyQt5 import QtGui, QtCore, QtWidgets as Qwid
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
from SCSA.SCSA import SCSA


class mainWindow(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        # GUI configuration
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.button = QtWidgets.QPushButton('Reconstruct', self)
        self.button2 = QtWidgets.QPushButton('Plot', self)
        self.addTab(self.tab1, "Graph 1")
        self.addTab(self.tab2, "Graph 2")
        self.figure1 = plt.figure(figsize=(10, 5))
        self.resize(1280, 720)
        self.canvas1 = FigureCanvas(self.figure1)

        self.figure2 = plt.figure(figsize=(10, 5))
        self.canvas2 = FigureCanvas(self.figure2)

        layout1 = QtWidgets.QVBoxLayout()
        layout1.addWidget(self.button)
        layout1.addWidget(self.canvas1)

        layout2 = QtWidgets.QVBoxLayout()
        layout2.addWidget(self.button2)
        layout2.addWidget(self.canvas2)

        self.tab1.setLayout(layout1)
        #self.addToolBar(NavigationToolbar(self.canvas1, self))
        self.tab2.setLayout(layout2)
        self.plot1()

        self.button.clicked.connect(self.plot2)
        self.button2.clicked.connect(self.plot3)

    def plot1(self):
        plt.ion()
        x = np.linspace(-5, 5, 512)
        data = np.exp(-x**2)*np.cos(2*np.pi*x)**2
        self.ax = self.figure1.add_subplot(211)
        self.ax.plot(data, 'b')
        self.canvas1.draw()

    def plot2(self):
        x = np.linspace(-5, 5, 512)
        h = np.arange(0.1, 3, 0.01)
        error = np.zeros(len(h))
        data = np.exp(-x**2)*np.cos(2*np.pi*x)**2
        for i in range(len(h)):
            holder = SCSA(data, h[i])
            error[i] = holder.mse
        holder = SCSA(data, h[error == min(error)])
        self.ax.plot(holder.reconstructed, 'k')
        error1 = np.square(data - holder.reconstructed)
        ay = self.figure1.add_subplot(212)
        ay.plot(error1)
        self.canvas1.draw()

    def plot3(self):
        x = np.arange(0, 10, 0.01)
        data = np.sinc(x)
        ax = self.figure2.add_subplot(111)
        ax.plot(x, data, 'k')
        self.canvas2.draw()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainw = mainWindow()
    mainw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
