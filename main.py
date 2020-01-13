from mainwindow import *
import pandas as pd
import sys


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui_elements()
        self.pushButton.clicked.connect(self.psi_graph)
        self.checkBox.stateChanged.connect(self.set_h_method)


    def ui_elements(self):
        self.radioButtonFunctions.toggled.connect(
            lambda: self.comboBoxFunctions.setEnabled(self.radioButtonFunctions.isChecked()))
        self.radioButtonManual.toggled.connect(lambda: self.lineEdit.setEnabled(self.radioButtonManual.isChecked()))
        self.radioButtonUserData.toggled.connect(self.set_enables)

    def psi_graph(self):
        indx1 = int(self.lineEdit_4.text()) - 1
        indx2 = int(self.lineEdit_3.text()) - 1
        indx3 = int(self.lineEdit_2.text()) - 1

        if indx1 > len(self.holder.km) - 1:
            indx1 = len(self.holder.km)
            self.lineEdit_4.setText(str(len(self.holder.km)))

        if indx1 < 0:
            indx1 = 0
            self.lineEdit_4.setText('1')

        if indx2 > len(self.holder.km) - 1:
            indx2 = len(self.holder.km)
            self.lineEdit_3.setText(str(len(self.holder.km)))

        if indx2 < 0:
            indx2 = 0
            self.lineEdit_2.setText('1')

        if indx3 > len(self.holder.km) - 1:
            indx3 = len(self.holder.km)
            self.lineEdit_2.setText(str(len(self.holder.km)))

        if indx3 < 0:
            indx3 = 0
            self.lineEdit_2.setText('1')

        psi1 = self.holder.psi[:, indx1]
        psi2 = self.holder.psi[:, indx2]
        psi3 = self.holder.psi[:, indx3]

        self.ap1.clear()
        self.ap2.clear()
        self.ap3.clear()

        self.ap1.plot(self.axis, np.square(psi1))
        self.ap2.plot(self.axis, np.square(psi2))
        self.ap3.plot(self.axis, np.square(psi3))

        self.ap1.set_title(r'$\Psi_' + '{' + str(indx1 + 1) + '}' + '^2(x)$')
        self.ap2.set_title(r'$\Psi_' + '{' + str(indx2 + 1) + '}' + '^2(x)$')
        self.ap3.set_title(r'$\Psi_' + '{' + str(indx3 + 1) + '}' + '^2(x)$')
        self.ap3.set_xlabel('$x$')

        self.canvasPsi.draw()

    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', "", "Text Files (*.txt)")
        if name[0] != '':
            self.holder.writeEigToTxt(str(name[0]))
            self.holder.writePsiToCsv(str(name[0][:-4]) + '_Psi.csv')

    def read_from_csv(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Read File', "", "CSV file (*.csv)")
        if name[0] != '':
            file = pd.read_csv(str(name[0]))
            self.axis_user = file.iloc[:, 0]
            self.signal_user = file.iloc[:, 1]
            self.radioButtonUserData.setEnabled(True)

    def set_enables(self):
        plt.ion()
        self.lineEditXmax.setEnabled(not self.radioButtonUserData.isChecked())
        self.lineEditXmin.setEnabled(not self.radioButtonUserData.isChecked())
        self.lineEditN.setEnabled(not self.radioButtonUserData.isChecked())
        self.pushButtonGraph.setEnabled(not self.radioButtonUserData.isChecked())
        self.ax.clear()
        self.ax.plot(self.axis_user, self.signal_user, label='Original')
        self.signal = self.signal_user
        self.axis = self.axis_user
        self.ax.set_title('$Signal \\ Reconstruction$')
        self.ax.set_xlabel('$x$')
        self.ax.legend()
        self.canvasGraph.draw()
        self.pushButtonReconstruct.setEnabled(True)

    def set_h_method(self):
        self.lineEditHmax.setEnabled(self.checkBox.isChecked())
        self.lineEditHmin.setEnabled(self.checkBox.isChecked())
        self.lineEditMh.setEnabled(self.checkBox.isChecked())
        self.lineEdith.setEnabled(not self.checkBox.isChecked())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())