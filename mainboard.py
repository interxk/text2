from PyQt5 import QtCore, QtGui, QtWidgets
from test2 import *
from test4 import *

class Shoye(QtWidgets.QMainWindow):
    def __init__(self):
        super(Shoye,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 814)
        MainWindow.setStyleSheet("background-image: url(D:/Users/yagvil/Desktop/python/softwareA/3.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 70, 321, 71))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 560, 161, 71))
        self.pushButton.setMinimumSize(QtCore.QSize(161, 71))
        self.pushButton.setStyleSheet("font: 24pt \"Arial Rounded MT Bold\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 560, 161, 71))
        self.pushButton_2.setMinimumSize(QtCore.QSize(161, 71))
        self.pushButton_2.setStyleSheet("font: 24pt \"Arial Rounded MT Bold\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.Picturetopicture)
        self.pushButton_2.clicked.connect(self.videotovideo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Microsoft Yahei\',\'sans-serif\',\'Arial\',\'Verdana\'; font-size:22pt; color:#64c8b8; background-color:#ffffff;\">Character painting</span></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">1</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "p2p"))
        self.pushButton_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">1</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "v2v"))

    def Picturetopicture(self):
        ui_hello_1.show()
        MainWindow.close()

    def videotovideo(self):
        ui_hello_2.show()
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Shoye()
    ui_hello_1= picturetopicture()
    ui_hello_2= sptosp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
