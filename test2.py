from PyQt5 import QtCore, QtGui, QtWidgets
from picture import p2p

class picturetopicture(QtWidgets.QMainWindow):
    def __init__(self):
        super(picturetopicture,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 271)
        MainWindow.setStyleSheet("background-image: url(D:/Users/yagvil/Desktop/yagewick/tuku/1.png);")#背景图片调用
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 211, 151))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 110, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(120, 100, 161, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)#生成的基本文件框类型

        self.commandLinkButton.clicked.connect(self.readpath)
        
        self.pushButton.clicked.connect(self.p2p)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">图片转换</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "转换"))
        self.commandLinkButton.setText(_translate("MainWindow", "文件路径选择"))
    def readpath(self):#利用文本框读取文件路径
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.lineEdit.setText(file_path)
    def p2p(self):
        path=self.lineEdit.text()
        p2p(path)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = picturetopicture()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
