import win32api
import win32con
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import threading
import time
import sys
import pyperclip
import keyboard

class Ui_MainWindow(object):
   
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('G:\\Users\\Henry\\Desktop\\Python\\R6 Akt code\\icon.ico')) 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.8125, y2:1, stop:0 rgba(41, 41, 61, 255), stop:1 rgba(32, 42, 72, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titlebar = QtWidgets.QWidget(self.frame)
        self.titlebar.setStyleSheet("background-color: rgb(35, 36, 45);")
        self.titlebar.setObjectName("titlebar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titlebar)
        self.horizontalLayout_2.setContentsMargins(8, 3, 8, 3)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.titlebar)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Lable_Title = QtWidgets.QLabel(self.widget_3)
        self.Lable_Title.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 700 15pt \"微軟正黑體\";")
        self.Lable_Title.setObjectName("Lable_Title")
        self.horizontalLayout.addWidget(self.Lable_Title)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.Btn_Hide = QtWidgets.QPushButton(self.titlebar)
        self.Btn_Hide.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_Hide.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_Hide.setStyleSheet("border-style:none;\n"
"border: none;\n"
"border-radius:7;\n"
"background-color: rgb(0, 255, 0);")
        self.Btn_Hide.setText("")
        self.Btn_Hide.setObjectName("Btn_Hide")
        self.horizontalLayout_2.addWidget(self.Btn_Hide, 0, QtCore.Qt.AlignRight)
        self.Btn_Close = QtWidgets.QPushButton(self.titlebar)
        self.Btn_Close.setMinimumSize(QtCore.QSize(15, 15))
        self.Btn_Close.setMaximumSize(QtCore.QSize(15, 15))
        self.Btn_Close.setStyleSheet("border-style:none;\n"
"border: none;\n"
"border-radius:7;\n"
"background-color: rgb(255, 0, 0);")
        self.Btn_Close.setText("")
        self.Btn_Close.setObjectName("Btn_Close")
        self.horizontalLayout_2.addWidget(self.Btn_Close, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout_3.addWidget(self.titlebar)
        self.main = QtWidgets.QWidget(self.frame)
        self.main.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.main.setObjectName("main")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_4.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.main)
        self.label.setStyleSheet("font: 700 11pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.Box_TextInput = QtWidgets.QTextEdit(self.main)
        self.Box_TextInput.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Box_TextInput.setStyleSheet("background-color:rgb(39, 36, 59) ;\n"
"color: rgb(200, 200, 200);\n"
"border-radius:10;\n"
"font: 12pt \"微軟正黑體\";\n"
"")
        self.Box_TextInput.setLineWidth(3)
        self.Box_TextInput.setObjectName("Box_TextInput")
        self.horizontalLayout_3.addWidget(self.Box_TextInput)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8outt = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8outt.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_8outt.setObjectName("horizontalLayout_8outt")
        self.label2 = QtWidgets.QLabel(self.main)
        self.label2.setStyleSheet("font: 700 11pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label2.setObjectName("label2")
        self.horizontalLayout_8outt.addWidget(self.label2)
        self.Box_TextOutput = QtWidgets.QTextEdit(self.main)
        self.Box_TextOutput.setStyleSheet("background-color:rgb(39, 36, 59) ;\n"
"color: rgb(200, 200, 200);\n"
"border-radius:10;\n"
"font: 12pt \"微軟正黑體\";\n"
"")
        self.Box_TextOutput.setObjectName("Box_TextOutput")
        self.horizontalLayout_8outt.addWidget(self.Box_TextOutput)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8outt)
        self.widget = QtWidgets.QWidget(self.main)
        self.widget.setStyleSheet("background-color: rgb(23, 23, 29);")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 8, 10, 5)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Lable_ver = QtWidgets.QLabel(self.widget)
        self.Lable_ver.setStyleSheet("font: 700 10pt \"微軟正黑體\";\n"
"color: rgb(200, 200, 200);")
        self.Lable_ver.setObjectName("Lable_ver")
        self.horizontalLayout_6.addWidget(self.Lable_ver)
        self.Btn_settings = QtWidgets.QPushButton(self.widget)
        self.Btn_settings.setMinimumSize(QtCore.QSize(20, 20))
        self.Btn_settings.setMaximumSize(QtCore.QSize(20, 20))
        self.Btn_settings.setStyleSheet("background-color: rgb(35, 36, 45);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 8pt \"微軟正黑體\";")
        self.Btn_settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("G:\\Users\\Henry\\Desktop\\Python\\R6 Akt code\\white-settings-icon-0.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_settings.setIcon(icon)
        self.Btn_settings.setIconSize(QtCore.QSize(10, 10))
        self.Btn_settings.setObjectName("Btn_settings")
        self.horizontalLayout_6.addWidget(self.Btn_settings, 0, QtCore.Qt.AlignRight)
        self.Btn_info = QtWidgets.QPushButton(self.widget)
        self.Btn_info.setMaximumSize(QtCore.QSize(20, 20))
        self.Btn_info.setStyleSheet("background-color: rgb(35, 36, 45);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 8pt \"微軟正黑體\";")
        self.Btn_info.setObjectName("Btn_info")
        self.horizontalLayout_6.addWidget(self.Btn_info, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_6.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CB_AutoType = QtWidgets.QCheckBox(self.widget)
        self.CB_AutoType.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(200, 200, 220);\n"
"")
        self.CB_AutoType.setObjectName("CB_AutoType")
        self.horizontalLayout_5.addWidget(self.CB_AutoType)
        self.CB_ChatDetector = QtWidgets.QCheckBox(self.widget)
        self.CB_ChatDetector.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(200, 200, 220);\n"
"")
        self.CB_ChatDetector.setObjectName("CB_ChatDetector")
        self.horizontalLayout_5.addWidget(self.CB_ChatDetector)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.Btn_Enter = QtWidgets.QPushButton(self.widget)
        self.Btn_Enter.setStyleSheet("background-color: rgb(68, 35, 177);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 16pt \"微軟正黑體\";")
        self.Btn_Enter.setAutoDefault(True)
        self.Btn_Enter.setDefault(True)
        self.Btn_Enter.setObjectName("Btn_Enter")
        self.horizontalLayout_4.addWidget(self.Btn_Enter)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout_3.addWidget(self.main)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def tips(self, state):
        if state == QtCore.Qt.Checked:
                QMessageBox.information(self,'提示',
                '''
                開啟聊天偵測模式時，
                右上角的綠色縮小按鈕會變成隱藏視窗的功能喲!    
                (使用T或Y來讓視窗顯示出來)
                '''
                , QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ALT-Code 轉換器"))
        self.titlebar.setToolTip(_translate("MainWindow", "縮小"))
        self.Lable_Title.setText(_translate("MainWindow", "ALT-Code 轉換器"))
        self.Btn_Close.setToolTip(_translate("MainWindow", "關閉"))
        self.label.setText(_translate("MainWindow", "文字:"))
        self.label2.setText(_translate("MainWindow", "輸出:"))
        self.Lable_ver.setText(_translate("MainWindow", "v1.0 by henry777 "))
        self.Btn_info.setText(_translate("MainWindow", "i"))
        self.CB_AutoType.setText(_translate("MainWindow", "自動輸入"))
        self.CB_ChatDetector.setText(_translate("MainWindow", "聊天偵測"))
        self.Btn_Enter.setText(_translate("MainWindow", "輸入"))
        self.Box_TextInput.setFocus() 
        self.CB_ChatDetector.stateChanged.connect(self.tips)
        def Btn_settings_clicked(): 
                QMessageBox.information(self,'設定',
                '''
                Comming soon!
                '''
                , QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)     

        def Btn_info_clicked(): 
                QMessageBox.information(self,'提示',
                '''
                目前自動輸入功能卡在驅動級別的按鍵模擬上!
                alt-code靠軟體模擬，是無法打出來的。
                '''
                , QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)                              
        def Btn_Enter_clicked():       
                print('Btn_Enter_clicked')

                def code(text):
                        big5text = text.encode('big5')
                        return (int.from_bytes(big5text, byteorder='big'))
                codelist=[]
                text = (self.Box_TextInput.toPlainText())
                if text !="":

                        print(F"\n輸入: {text}\n")
                        for i in range(len(text)):
                                big5int=code(text[i])
                                codelist.append(big5int)
                        self.Box_TextOutput.setPlainText(str(codelist))
                                
                        print(F"\n輸出: {codelist}\n")      
                if self.CB_AutoType.isChecked():
                        print(self.CB_AutoType.isChecked)


                        def autotype():
                                print("autotype")
                                time.sleep( 2 )
                                for i in range(len(codelist)):
                                        win32api.keybd_event(18,0,0,0)  # ALT
                                        for c in range(len(str(codelist[i]))):
                                                temp=int(str(codelist[i])[c])+96
                                                win32api.keybd_event(temp, 2)
                                                win32api.keybd_event(temp, 0,win32con.KEYEVENTF_KEYUP,0)
                                        win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
                        t = threading.Thread(target = autotype)
                        t.start()  
                      

        def greenbutton():
                if self.CB_ChatDetector.isChecked():
                        MainWindow.hide()
                else:
                        MainWindow.showMinimized()
        self.Btn_Close.clicked.connect(QtWidgets.qApp.quit)
        self.Btn_Hide.clicked.connect(greenbutton)
        self.Btn_Enter.clicked.connect(Btn_Enter_clicked)
        self.Btn_settings.clicked.connect(Btn_settings_clicked)
        self.Btn_info.clicked.connect(Btn_info_clicked)
        def job():   
                def AllChatPressed():
                        MainWindow.activateWindow()
                        if MainWindow is not None and MainWindow.windowState() != QtCore.Qt.WindowActive:  
                                print('AllChatPressed')   
                                MainWindow.show()
                                
                def TeamChatPressed():
                        MainWindow.activateWindow()
                        if MainWindow is not None and MainWindow.windowState() != QtCore.Qt.WindowActive:    
                                print('TeamChatPressed')  
                                MainWindow.show()              
                        MainWindow.show()
                keyboard.add_hotkey('t', AllChatPressed)
                keyboard.add_hotkey('y', TeamChatPressed)

        t = threading.Thread(target = job)
        t.start()

class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
    def mousePressEvent(self, event):                                
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                                  
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()        




        
