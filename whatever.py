# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from sympy import *

from scipy.special import dawsn

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar

from SCSA.SCSA import SCSA



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 576)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(190, 0, 601, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 250, 61, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 59, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEditHmin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditHmin.setGeometry(QtCore.QRect(70, 250, 113, 21))
        self.lineEditHmin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditHmin.setObjectName("lineEditHmin")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 61, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEditHmax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditHmax.setGeometry(QtCore.QRect(70, 280, 113, 21))
        self.lineEditHmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditHmax.setObjectName("lineEditHmax")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEditN = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditN.setGeometry(QtCore.QRect(70, 130, 113, 21))
        self.lineEditN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditN.setObjectName("lineEditN")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEditXmin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditXmin.setGeometry(QtCore.QRect(70, 70, 113, 21))
        self.lineEditXmin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditXmin.setObjectName("lineEditXmin")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 61, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditMh = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMh.setGeometry(QtCore.QRect(70, 310, 113, 21))
        self.lineEditMh.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMh.setObjectName("lineEditMh")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEditXmax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditXmax.setGeometry(QtCore.QRect(70, 100, 113, 21))
        self.lineEditXmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditXmax.setObjectName("lineEditXmax")
        self.pushButtonReconstruct = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReconstruct.setGeometry(QtCore.QRect(40, 350, 121, 32))
        self.pushButtonReconstruct.setObjectName("pushButtonReconstruct")
        self.pushButtonGraph = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGraph.setGeometry(QtCore.QRect(40, 170, 121, 32))
        self.pushButtonGraph.setObjectName("pushButtonGraph")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_eigenvalues_and_eigenfunctions = QtWidgets.QAction(MainWindow)
        self.actionSave_eigenvalues_and_eigenfunctions.setObjectName("actionSave_eigenvalues_and_eigenfunctions")
        self.actionLoad_data_csv = QtWidgets.QAction(MainWindow)
        self.actionLoad_data_csv.setObjectName("actionLoad_data_csv")
        self.menuFile.addAction(self.actionSave_eigenvalues_and_eigenfunctions)
        self.menuFile.addAction(self.actionLoad_data_csv)
        self.menubar.addAction(self.menuFile.menuAction())

        self.figureGraph = plt.figure(figsize=(10, 5))
        self.figureError = plt.figure(figsize=(10, 5))

        self.canvasGraph = FigureCanvas(self.figureGraph)
        self.canvasError = FigureCanvas(self.figureError)

        self.ax = self.figureGraph.add_subplot(111)
        self.ay = self.figureError.add_subplot(211)
        self.az = self.figureError.add_subplot(212)

        self.toolbarGraph = NavigationToolbar(self.canvasGraph, self.tab)
        self.toolbarError = NavigationToolbar(self.canvasError, self.tab_2)

        layoutGraph = QtWidgets.QVBoxLayout()
        layoutGraph.addWidget(self.canvasGraph)
        layoutGraph.addWidget(self.toolbarGraph)

        layoutError = QtWidgets.QVBoxLayout()
        layoutError.addWidget(self.canvasError)
        layoutError.addWidget(self.toolbarError)

        self.tab.setLayout(layoutGraph)
        self.tab_2.setLayout(layoutError)

        self.pushButtonGraph.clicked.connect(self.graph)
        self.pushButtonReconstruct.clicked.connect(self.reconstruct)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Reconstruction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Errors"))
        self.lineEdit.setText(_translate("MainWindow", "exp(-x**2)*cos(2*pi*x)**2"))
        self.label.setText(_translate("MainWindow", "h_min"))
        self.label_2.setText(_translate("MainWindow", "Equation"))
        self.lineEditHmin.setText(_translate("MainWindow", "0.01"))
        self.label_3.setText(_translate("MainWindow", "h_max"))
        self.lineEditHmax.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "N"))
        self.lineEditN.setText(_translate("MainWindow", "256"))
        self.label_5.setText(_translate("MainWindow", "x_min"))
        self.lineEditXmin.setText(_translate("MainWindow", "-5"))
        self.label_6.setText(_translate("MainWindow", "M_h"))
        self.lineEditMh.setText(_translate("MainWindow", "200"))
        self.label_7.setText(_translate("MainWindow", "X_max"))
        self.lineEditXmax.setText(_translate("MainWindow", "5"))
        self.pushButtonReconstruct.setText(_translate("MainWindow", "Reconstruct"))
        self.pushButtonGraph.setText(_translate("MainWindow", "Graph equation"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_eigenvalues_and_eigenfunctions.setText(_translate("MainWindow", "Save eigenvalues and eigenfunctions"))
        self.actionLoad_data_csv.setText(_translate("MainWindow", "Load data (.csv)"))

        self.pushButtonReconstruct.setEnabled(False)

    def reconstruct(self):

        hmin = float(self.lineEditHmin.text())
        hmax = float(self.lineEditHmax.text())
        Mh = int(self.lineEditMh.text())
        h = np.linspace(hmin, hmax, Mh)
        error = np.linspace(0, 0, Mh)
        for i in range(Mh):
            holder = SCSA(self.signal, h[i])
            error[i] = holder.mse
        holder = SCSA(self.signal, h[error == min(error)])
        self.ax.plot(self.axis, holder.reconstructed, 'k')
        errorGraph = np.square(self.signal - holder.reconstructed)/np.max(self.signal)

        self.ay.clear()
        self.az.clear()
        self.ay.plot(self.axis, errorGraph)
        self.az.plot(h, error)
        self.canvasError.draw()

    def graph(self):
        plt.ion()
        self.ax.clear()
        x = symbols('x')
        equation = self.lineEdit.text()
        xmax = float(self.lineEditXmax.text())
        xmin = float(self.lineEditXmin.text())
        N = int(self.lineEditN.text())
        self.axis = np.linspace(xmin, xmax, N)
        f = lambdify(x, equation, "numpy")
        self.signal = f(self.axis)
        self.ax.plot(self.axis, self.signal)
        self.canvasGraph.draw()
        self.pushButtonReconstruct.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
