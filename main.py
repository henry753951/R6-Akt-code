import time
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from output import Ui_MainWindow,MyWin




if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
    w = MyWin()
    w.show()
    sys.exit(app.exec_())







