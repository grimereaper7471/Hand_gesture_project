# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcomepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from subprocess import Popen


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 85)
        Form.setMinimumSize(QtCore.QSize(410, 85))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.Welcom_Register_Btn = QtWidgets.QPushButton(Form)
        self.Welcom_Register_Btn.setObjectName("Welcom_Register_Btn")
        self.gridLayout.addWidget(self.Welcom_Register_Btn, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.Welcom_Login_Btn = QtWidgets.QPushButton(Form)
        self.Welcom_Login_Btn.setObjectName("Welcom_Login_Btn")
        self.gridLayout.addWidget(self.Welcom_Login_Btn, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the buttons to their respective functions
        self.Welcom_Register_Btn.clicked.connect(self.open_register_page)
        self.Welcom_Login_Btn.clicked.connect(self.open_login_page)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Welcom_Register_Btn.setText(_translate("Form", "To Register Page"))
        self.label.setText(_translate("Form", "Welcome to Hand Gesture Recogoition "))
        self.Welcom_Login_Btn.setText(_translate("Form", "To Login Page"))

    def open_register_page(self):
        Form.hide()
        Popen(["python", "Registerpage.py"])

    def open_login_page(self):
        Form.hide()
        Popen(["python", "LoginPage.py"])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
