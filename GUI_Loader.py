import sys
from datetime import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
from Database_functions import Functions
from UI.Python_UI.Test_login import Ui_Form
import numpy as np
import sqlite3
import re

class Login_screen(QtWidgets.QWidget):
    def __init__(self):
        super(Login_screen,self).__init__()
        self.ui1 = Ui_Form()
        self.ui1.setupUi(self)

        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Login_screen()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        
        