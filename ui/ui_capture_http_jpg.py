# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_capture_http_jpg.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 754)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame_2)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.horizontalLayout_4.addWidget(self.webEngineView)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.httpJpgPicRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.httpJpgPicRadioButton.setGeometry(QtCore.QRect(40, 110, 115, 19))
        self.httpJpgPicRadioButton.setObjectName("httpJpgPicRadioButton")
        self.httpJpgStreamRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.httpJpgStreamRadioButton.setGeometry(QtCore.QRect(40, 140, 115, 19))
        self.httpJpgStreamRadioButton.setObjectName("httpJpgStreamRadioButton")
        self.httpJpgCapturePushButton = QtWidgets.QPushButton(self.frame_3)
        self.httpJpgCapturePushButton.setGeometry(QtCore.QRect(30, 190, 93, 28))
        self.httpJpgCapturePushButton.setObjectName("httpJpgCapturePushButton")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.httpJpgPicRadioButton.setText(_translate("MainWindow", "Pic"))
        self.httpJpgStreamRadioButton.setText(_translate("MainWindow", "Stream"))
        self.httpJpgCapturePushButton.setText(_translate("MainWindow", "Capture"))
from PyQt5 import QtWebEngineWidgets