import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 600)
    w.move(0, 0)
    w.setWindowTitle('Mi primera ventana en qt')
    w.show()

    sys.exit(app.exec_())