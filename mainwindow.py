# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from sympy import *
from scipy.special import dawsn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from SCSA.SCSA import SCSA, diffMatrix


def weierstrass(x, a, b):
    y = np.zeros(len(x))
    for i in range(12):
        y += (a**i)*np.cos((b**i)*np.pi*x)

    return y


class WorkerSignals(QtCore.QObject):
    '''
        Defines the signals available from a running worker thread.

        Supported signals are:

        finished
            No data

        error
            `tuple` (exctype, value, traceback.format_exc() )

        result
            `object` data returned from processing, anything

        progress
            `int` indicating % progress

    '''
    finished = QtCore.pyqtSignal(object)
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)


class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, D, signal, h, Mh):
        super(Worker, self).__init__()
        self.h = h
        self.D = D
        self.signal = signal
        self.Mh = Mh
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        error = np.linspace(0, 0, self.Mh)
        try:
            for i in range(self.Mh):
                holder = SCSA(D=self.D, signal=self.signal, h=self.h[i])
                error[i] = holder.mse
                self.signals.progress.emit(i)
        except:
            print('Something went wrong')
        else:
            self.signals.finished.emit(error)  # Done


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonGraph = QtWidgets.QPushButton(self.tab)
        self.pushButtonGraph.setObjectName("pushButtonGraph")
        self.horizontalLayout_4.addWidget(self.pushButtonGraph)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.comboBoxFunctions = QtWidgets.QComboBox(self.tab)
        self.comboBoxFunctions.setObjectName("comboBoxFunctions")
        self.comboBoxFunctions.addItem("")
        self.comboBoxFunctions.addItem("")
        self.comboBoxFunctions.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxFunctions)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButtonReconstruct = QtWidgets.QPushButton(self.tab)
        self.pushButtonReconstruct.setObjectName("pushButtonReconstruct")
        self.verticalLayout_6.addWidget(self.pushButtonReconstruct)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 8, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditHmin = QtWidgets.QLineEdit(self.tab)
        self.lineEditHmin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditHmin.setObjectName("lineEditHmin")
        self.gridLayout_2.addWidget(self.lineEditHmin, 1, 1, 1, 1)
        self.lineEditHmax = QtWidgets.QLineEdit(self.tab)
        self.lineEditHmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditHmax.setObjectName("lineEditHmax")
        self.gridLayout_2.addWidget(self.lineEditHmax, 2, 1, 1, 1)
        self.lineEditMh = QtWidgets.QLineEdit(self.tab)
        self.lineEditMh.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMh.setObjectName("lineEditMh")
        self.gridLayout_2.addWidget(self.lineEditMh, 3, 1, 1, 1)
        self.lineEdith = QtWidgets.QLineEdit(self.tab)
        self.lineEdith.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdith.setObjectName("lineEdith")
        self.gridLayout_2.addWidget(self.lineEdith, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 7, 0, 1, 1)
        self.layout_reconstruction_plot = QtWidgets.QVBoxLayout()
        self.layout_reconstruction_plot.setObjectName("layout_reconstruction_plot")
        self.gridLayout_4.addLayout(self.layout_reconstruction_plot, 0, 1, 9, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditN = QtWidgets.QLineEdit(self.tab)
        self.lineEditN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditN.setObjectName("lineEditN")
        self.gridLayout.addWidget(self.lineEditN, 2, 1, 1, 1)
        self.lineEditXmax = QtWidgets.QLineEdit(self.tab)
        self.lineEditXmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditXmax.setObjectName("lineEditXmax")
        self.gridLayout.addWidget(self.lineEditXmax, 1, 1, 1, 1)
        self.lineEditXmin = QtWidgets.QLineEdit(self.tab)
        self.lineEditXmin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditXmin.setObjectName("lineEditXmin")
        self.gridLayout.addWidget(self.lineEditXmin, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonManual = QtWidgets.QRadioButton(self.tab)
        self.radioButtonManual.setObjectName("radioButtonManual")
        self.verticalLayout.addWidget(self.radioButtonManual)
        self.radioButtonFunctions = QtWidgets.QRadioButton(self.tab)
        self.radioButtonFunctions.setObjectName("radioButtonFunctions")
        self.verticalLayout.addWidget(self.radioButtonFunctions)
        self.radioButtonUserData = QtWidgets.QRadioButton(self.tab)
        self.radioButtonUserData.setObjectName("radioButtonUserData")
        self.verticalLayout.addWidget(self.radioButtonUserData)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_5.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_5.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 3, 1, 1, 1)
        self.labelPlotPsi1 = QtWidgets.QLabel(self.tab_3)
        self.labelPlotPsi1.setObjectName("labelPlotPsi1")
        self.gridLayout_5.addWidget(self.labelPlotPsi1, 0, 2, 1, 1)
        self.labelPlotPsi2_2 = QtWidgets.QLabel(self.tab_3)
        self.labelPlotPsi2_2.setObjectName("labelPlotPsi2_2")
        self.gridLayout_5.addWidget(self.labelPlotPsi2_2, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.labelPlotPsi2 = QtWidgets.QLabel(self.tab_3)
        self.labelPlotPsi2.setObjectName("labelPlotPsi2")
        self.gridLayout_5.addWidget(self.labelPlotPsi2, 1, 2, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_5)
        self.psiLayout = QtWidgets.QVBoxLayout()
        self.psiLayout.setObjectName("psiLayout")
        self.horizontalLayout_6.addLayout(self.psiLayout)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 22))
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

        self.lineEdit.setMinimumWidth(170)

        # Life improvements

        self.actionSave_eigenvalues_and_eigenfunctions.setShortcut("Ctrl+S")
        self.actionSave_eigenvalues_and_eigenfunctions.setStatusTip('Save File')
        self.actionSave_eigenvalues_and_eigenfunctions.triggered.connect(self.file_save)

        self.actionLoad_data_csv.setShortcut("Ctrl+O")
        self.actionLoad_data_csv.setStatusTip("Load data from a .csv file")
        self.actionLoad_data_csv.triggered.connect(self.read_from_csv)

        # Graphing stuff

        self.figureGraph = plt.figure(figsize=(15, 10))
        self.figureError = plt.figure(figsize=(15, 10))
        self.figurePsi = plt.figure(figsize=(15, 10))

        self.canvasGraph = FigureCanvas(self.figureGraph)
        self.canvasError = FigureCanvas(self.figureError)
        self.canvasPsi = FigureCanvas(self.figurePsi)

        self.ax = self.figureGraph.add_subplot(111)
        self.ay = self.figureError.add_subplot(211)
        self.az = self.figureError.add_subplot(212)

        self.ap1 = self.figurePsi.add_subplot(311)
        self.ap1.axes.get_xaxis().set_visible(False)
        self.ap2 = self.figurePsi.add_subplot(312)
        self.ap2.axes.get_xaxis().set_visible(False)
        self.ap3 = self.figurePsi.add_subplot(313)

        self.toolbarGraph = NavigationToolbar(self.canvasGraph, self.tab)
        self.toolbarError = NavigationToolbar(self.canvasError, self.tab_2)
        self.toolbarPsi = NavigationToolbar(self.canvasPsi, self.tab_3)

        self.layout_reconstruction_plot.addWidget(self.canvasGraph)
        self.layout_reconstruction_plot.addWidget(self.toolbarGraph)

        layoutError = QtWidgets.QVBoxLayout()
        layoutError.addWidget(self.canvasError)
        layoutError.addWidget(self.toolbarError)

        self.psiLayout.addWidget(self.canvasPsi)
        self.psiLayout.addWidget(self.toolbarPsi)

        self.tab_2.setLayout(layoutError)

        self.pushButtonGraph.clicked.connect(self.graph)
        self.pushButtonReconstruct.clicked.connect(self.reconstruct)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.threadpool = QtCore.QThreadPool()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonGraph.setText(_translate("MainWindow", "Graph equation"))
        self.label_2.setText(_translate("MainWindow", "Equation"))
        self.lineEdit.setText(_translate("MainWindow", "exp(-abs(x))*cos(x)**2"))
        self.label_8.setText(_translate("MainWindow", "SP Functions"))
        self.comboBoxFunctions.setItemText(0, _translate("MainWindow", "Dawson Integral"))
        self.comboBoxFunctions.setItemText(1, _translate("MainWindow", "Weierstrass function"))
        self.comboBoxFunctions.setItemText(2, _translate("MainWindow", "Rectangular pulse"))
        self.pushButtonReconstruct.setText(_translate("MainWindow", "Reconstruct"))
        self.label_6.setText(_translate("MainWindow", "M_h"))
        self.label_9.setText(_translate("MainWindow", "h"))
        self.label_3.setText(_translate("MainWindow", "h_max"))
        self.label.setText(_translate("MainWindow", "h_min"))
        self.lineEditHmin.setText(_translate("MainWindow", "0.01"))
        self.lineEditHmax.setText(_translate("MainWindow", "3"))
        self.lineEditMh.setText(_translate("MainWindow", "200"))
        self.lineEdith.setText(_translate("MainWindow", "1"))
        self.lineEditN.setText(_translate("MainWindow", "256"))
        self.lineEditXmax.setText(_translate("MainWindow", "5"))
        self.lineEditXmin.setText(_translate("MainWindow", "-5"))
        self.lineEdit_2.setText(_translate("MainWindow", "3"))
        self.lineEdit_3.setText(_translate("MainWindow", "2"))
        self.lineEdit_4.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "x_min"))
        self.label_7.setText(_translate("MainWindow", "x_max"))
        self.label_4.setText(_translate("MainWindow", "N"))
        self.radioButtonManual.setText(_translate("MainWindow", "Manually typing"))
        self.radioButtonFunctions.setText(_translate("MainWindow", "Sp Functions"))
        self.radioButtonUserData.setText(_translate("MainWindow", "User data"))
        self.checkBox.setText(_translate("MainWindow", "Automatic h iteration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Reconstruction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Errors"))
        self.label_10.setText(_translate("MainWindow", "First plot"))
        self.label_12.setText(_translate("MainWindow", "Third plot"))
        self.pushButton.setText(_translate("MainWindow", "Graph"))
        self.labelPlotPsi1.setText(_translate("MainWindow", "TextLabel"))
        self.labelPlotPsi2_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "Second plot"))
        self.labelPlotPsi2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Psi"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_eigenvalues_and_eigenfunctions.setText(_translate("MainWindow", "Save eigenvalues and eigenfunctions"))
        self.actionLoad_data_csv.setText(_translate("MainWindow", "Load data (.csv)"))

        self.pushButtonReconstruct.setEnabled(False)
        self.radioButtonManual.setChecked(True)
        self.radioButtonFunctions.setChecked(False)
        self.comboBoxFunctions.setEnabled(False)
        self.actionSave_eigenvalues_and_eigenfunctions.setEnabled(False)
        self.radioButtonUserData.setEnabled(False)
        self.tab_2.setEnabled(False)
        self.tab_3.setEnabled(False)
        self.lineEditMh.setEnabled(False)
        self.lineEditHmin.setEnabled(False)
        self.lineEditHmax.setEnabled(False)

    def reconstruct(self):
        self.pushButtonReconstruct.setEnabled(False)
        self.D = diffMatrix(len(self.signal), method='fourier')
        if self.checkBox.isChecked():
            hmin = float(self.lineEditHmin.text())
            hmax = float(self.lineEditHmax.text())
            self.Mh = int(self.lineEditMh.text())
            self.h = np.linspace(hmin, hmax, self.Mh)

            worker = Worker(self.D, self.signal, self.h, self.Mh)

            worker.signals.progress.connect(self.oniterationupdate)
            worker.signals.finished.connect(self.workerfinished)

            self.threadpool.start(worker)
        else:
            self.h = float(self.lineEdith.text())
            self.workerfinished(error=None)

    def workerfinished(self, error=None):
        #Clearing axes
        self.ax.clear()
        self.ay.clear()
        self.az.clear()

        #auto reconstruction or single-h representation
        if error == None:
            self.holder = SCSA(self.D, self.signal, self.h)
            self.ax.plot(self.axis, self.signal, label='Original')
            self.ax.plot(self.axis, self.holder.reconstructed, 'k', label='Reconstructed')
            self.ax.legend()
            self.ax.set_title('$Signal \\ Reconstruction$')
            self.ax.set_xlabel('$x$')

            errorGraph = np.square(self.signal - self.holder.reconstructed) / np.max(self.signal)
            self.ay.plot(self.axis, errorGraph)
            self.ay.set_xlabel('$X$')
            self.ay.set_ylabel(r'$\frac{(y^i - y^i_h)^2}{y_{max}}$')
            self.canvasError.draw()
        else:

            self.holder = SCSA(self.D, self.signal, self.h[error == np.min(error)])
            self.ax.plot(self.axis, self.signal, label='Original')
            self.ax.plot(self.axis, self.holder.reconstructed, 'k', label='Reconstructed')
            self.ax.legend()
            self.ax.set_title('$Signal \\ Reconstruction$')
            self.ax.set_xlabel('$x$')

            errorGraph = np.square(self.signal - self.holder.reconstructed) / np.max(self.signal)
            self.ay.plot(self.axis, errorGraph)
            self.ay.set_xlabel('$X$')
            self.ay.set_ylabel('$(y^i - y^i_h)^2$')
            self.az.plot(self.h, error)
            self.az.set_xlabel('$h$')
            self.az.set_ylabel('$MSE$')
            self.canvasError.draw()

        text = '1 <= i <=' + ' ' + str(len(self.holder.km))

        self.labelPlotPsi1.setText(text)
        self.labelPlotPsi2.setText(text)
        self.labelPlotPsi2_2.setText(text)

        self.pushButtonReconstruct.setEnabled(True)
        self.actionSave_eigenvalues_and_eigenfunctions.setEnabled(True)
        self.tab_2.setEnabled(True)
        self.tab_3.setEnabled(True)

    def graph(self):
        self.ax.clear()
        plt.ion()
        equation = self.lineEdit.text()
        xmax = float(self.lineEditXmax.text())
        xmin = float(self.lineEditXmin.text())
        N = int(self.lineEditN.text())
        self.axis = np.linspace(xmin, xmax, N)
        if self.radioButtonFunctions.isChecked() == False:
            x = symbols('x')
            f = lambdify(x, equation, "numpy")
            signal = f(self.axis)
        else:
            if self.comboBoxFunctions.currentIndex() == 0:
                signal = dawsn(self.axis)
            elif self.comboBoxFunctions.currentIndex() == 1:
                signal = weierstrass(self.axis, 0.5, 7)
            else:
                signal = (np.sign(np.sin(np.pi*self.axis)) + 1)/2

        self.signal = signal
        self.ax.plot(self.axis, self.signal, label='Original')
        self.ax.legend()
        self.ax.set_title('$Signal \\ Reconstruction$')
        self.ax.set_xlabel('$x$')

        self.canvasGraph.draw()
        self.pushButtonReconstruct.setEnabled(True)

    def oniterationupdate(self, i):
        self.progressBar.setValue(np.round(i*100/self.Mh))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
