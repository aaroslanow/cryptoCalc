__author__ = 'Adam'


from PyQt4.QtGui import QApplication, QDialog
from gui import Ui_Dialog
from PyQt4 import QtCore, QtGui
import sys
from functools import partial
import encryption
import hashes
import Tkinter,tkFileDialog
import parity
import ctypes

class Main_Window(QtGui.QMainWindow):
    mode_Value = None
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        ui = Ui_Dialog()
        ui.setupUi(self)

        ui.EncryptButton.clicked.connect(partial(self.handleEncryptButton,ui))
        ui.DecryptButton.clicked.connect(partial(self.handleDecryptButton,ui))
        ui.Text_Go_Btn.clicked.connect(partial(self.handleText_GO_BTN,ui))
        ui.Sel_File_Btn.clicked.connect(partial(self.set_filePath,ui))
        ui.File_Go_Btn.clicked.connect(partial(self.handleFile_GO_BTN,ui))
        ui.lineEdit_6.setText("0000000000000000")
        ui.comboBox.currentIndexChanged.connect(partial(self.vectordeactivate,ui))
        ui.AlgoBox.currentIndexChanged.connect(partial(self.changeLabels,ui))
        ui.KCVButton.clicked.connect(partial(self.KCVOnly,ui))
        ui.Check_Parity_BTN.clicked.connect(partial(self.checkParity,ui))
        ui.COMP_PArity_Btn.clicked.connect(partial(self.computeParity,ui))

    def handleEncryptButton(self,ui):
        algo = str(ui.AlgoBox.currentText())
        mode = str(ui.comboBox.currentText())
        input = str(ui.DataText.text())
        self.checkInput(input)
        key = str(ui.KeyText.text())
        iv = str(ui.lineEdit_6.text())
        if algo == "DES":
            result = encryption.Des_Encrypt(mode,input,key,iv)
            ui.ResultText.setText(result.encode('hex'))
            KCV = encryption.compute_KCV(key)
            ui.KCVTEXT.setText(KCV.encode('hex')[0:6])
        elif algo =="AES":
            result=encryption.AES_encryption(mode,input,key)
            ui.ResultText.setText(result.encode('hex'))
            KCV = encryption.compute_KCV(key)
            ui.KCVTEXT.setText(KCV.encode('hex')[0:6])
        elif algo == "3DES":
            result = encryption.triple_Des_encrypt(mode,input,key,iv)
            ui.ResultText.setText(result.encode('hex'))
            KCV = encryption.compute_KCV(key)
            ui.KCVTEXT.setText(KCV.encode('hex')[0:6])
        elif algo == "XOR":
            result = encryption.xor_calc(input,key)
            ui.ResultText.setText(result.encode('hex'))


    def handleDecryptButton(self,ui):
        iv = str(ui.lineEdit_6.text())
        algo = str(ui.AlgoBox.currentText())
        mode = str(ui.comboBox.currentText())
        input = str(ui.DataText.text())
        key = str(ui.KeyText.text())
        self.checkInput(input)
        if algo == "DES":
            result = encryption.Des_Decrypt(mode,input,key,iv)
            ui.ResultText.setText(result.encode('hex').rstrip('0'))
            KCV = encryption.compute_KCV(key.encode('hex'))
            ui.KCVTEXT.setText(KCV.encode('hex')[0:6])
        elif algo == "AES":
            result=encryption.AES_decryption(mode,input,key)
            ui.ResultText.setText(result.encode('hex'))
            KCV = encryption.compute_KCV(key)
            ui.KCVTEXT.setText(KCV.encode('hex')[0:6])
        elif algo  == "3DES":
            result = encryption.triple_Des_Decrypt(mode,input,key,iv)
            ui.ResultText.setText(result.encode('hex'))
            KCV = encryption.compute_KCV(key)
            ui.KCVTEXT.setText(KCV.encode('hex')[0:6])

    def handleText_GO_BTN(self,ui):
        textInput = str(ui.lineEdit.text())
        result=hashes.getSHA1_Text(textInput)
        ui.lineEdit_3.setText(result)

    def set_filePath(self,ui):
        home = "C:\\"
        fileDialog = Tkinter.Tk()
        fileDialog.withdraw()
        ui.lineEdit_2.setText(str(tkFileDialog.askopenfilename(initialdir =home)))

    def handleFile_GO_BTN(self,ui):
        filepath = str(ui.lineEdit_2.text())
        result = hashes.getSHA1_File(filepath)
        ui.lineEdit_3.setText(result)

    def KCVOnly(self,ui):
        key = str(ui.KeyText.text())
        self.checkInput(key)
        KCV = encryption.compute_KCV(key)
        ui.KCVTEXT.setText(KCV.encode('hex')[0:6])

    def vectordeactivate(self,ui):
        mode = str(ui.comboBox.currentText())
        if mode == "CBC":
            ui.lineEdit_6.setEnabled(True)
        else:
            ui.lineEdit_6.setEnabled(False)

    def changeLabels(self,ui):
        algo = str(ui.AlgoBox.currentText())
        if algo == "XOR":
            ui.DataLabel.setText("Data 1")
            ui.KeyLabel.setText("Data 2")

        else:
            ui.DataLabel.setText("Data")
            ui.KeyLabel.setText("Key")

    def checkParity(self,ui):
        input = str(ui.lineEdit_4.text())
        self.checkInput(input)
        result =parity.check_parity(input)
        ui.lineEdit_5.setText(result)

    def computeParity(self,ui):
        input = str(ui.lineEdit_4.text())
        self.checkInput(input)
        mode = str(ui.comboBox_2.currentText())
        result=parity.compute_parity(mode,input)
        ui.lineEdit_5.setText(result)

    def checkInput(self,input):
        try:
          result= int(input,16)
        except ValueError as ex:
            ctypes.windll.user32.MessageBoxW(0,u"Input value is not hexadecimal",u"Error",0)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Main_Window()
    myapp.show()
    sys.exit(app.exec_())


