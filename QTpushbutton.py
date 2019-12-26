from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, \
    QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 Window'
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 400

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setToolTip('This is <b> My first window </b>')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.uiComponents()
        self.show()

    def uiComponents(self):
        button = QPushButton('Click Me', self)
        button.setToolTip('This is my <b> first tooltip </b> ')
        #button.move(50, 50)
        button.setGeometry(QRect(100, 100, 120, 36))
        button.clicked.connect(self.clickMe)

    def clickMe(self):
        sys.exit()

    def createLayout(self):
        self.groupBox = QGroupBox('What is your favorite PStar?')
        hboxlayout = QHBoxLayout()

        button = QPushButton('Click Me', self)
        button.setToolTip('This is my <b> first tooltip </b> ')
        # button.move(50, 50)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
