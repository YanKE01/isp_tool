# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1618, 894)
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
        self.frame_2.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.algorithmListWidget = QtWidgets.QListWidget(self.frame_2)
        self.algorithmListWidget.setObjectName("algorithmListWidget")
        item = QtWidgets.QListWidgetItem()
        self.algorithmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.algorithmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.algorithmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.algorithmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.algorithmListWidget.addItem(item)
        self.horizontalLayout_5.addWidget(self.algorithmListWidget)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.parameterStackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameterStackedWidget.sizePolicy().hasHeightForWidth())
        self.parameterStackedWidget.setSizePolicy(sizePolicy)
        self.parameterStackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.parameterStackedWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.parameterStackedWidget.setObjectName("parameterStackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.manualOffsetRSpinBox = QtWidgets.QSpinBox(self.page)
        self.manualOffsetRSpinBox.setMaximum(4095)
        self.manualOffsetRSpinBox.setObjectName("manualOffsetRSpinBox")
        self.horizontalLayout_9.addWidget(self.manualOffsetRSpinBox)
        self.manualOffsetRHorizontalSlider = QtWidgets.QSlider(self.page)
        self.manualOffsetRHorizontalSlider.setMaximum(4095)
        self.manualOffsetRHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.manualOffsetRHorizontalSlider.setObjectName("manualOffsetRHorizontalSlider")
        self.horizontalLayout_9.addWidget(self.manualOffsetRHorizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.manualOffsetGrSpinBox = QtWidgets.QSpinBox(self.page)
        self.manualOffsetGrSpinBox.setMaximum(4095)
        self.manualOffsetGrSpinBox.setObjectName("manualOffsetGrSpinBox")
        self.horizontalLayout_10.addWidget(self.manualOffsetGrSpinBox)
        self.manualOffsetGrHorizontalSlider = QtWidgets.QSlider(self.page)
        self.manualOffsetGrHorizontalSlider.setMaximum(4095)
        self.manualOffsetGrHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.manualOffsetGrHorizontalSlider.setObjectName("manualOffsetGrHorizontalSlider")
        self.horizontalLayout_10.addWidget(self.manualOffsetGrHorizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.manualOffsetGbSpinBox = QtWidgets.QSpinBox(self.page)
        self.manualOffsetGbSpinBox.setMaximum(4095)
        self.manualOffsetGbSpinBox.setObjectName("manualOffsetGbSpinBox")
        self.horizontalLayout_11.addWidget(self.manualOffsetGbSpinBox)
        self.manualOffsetGbHorizontalSlider = QtWidgets.QSlider(self.page)
        self.manualOffsetGbHorizontalSlider.setMaximum(4095)
        self.manualOffsetGbHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.manualOffsetGbHorizontalSlider.setObjectName("manualOffsetGbHorizontalSlider")
        self.horizontalLayout_11.addWidget(self.manualOffsetGbHorizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.manualOffsetBSpinBox = QtWidgets.QSpinBox(self.page)
        self.manualOffsetBSpinBox.setMaximum(4095)
        self.manualOffsetBSpinBox.setObjectName("manualOffsetBSpinBox")
        self.horizontalLayout_12.addWidget(self.manualOffsetBSpinBox)
        self.manualOffsetBHorizontalSlider = QtWidgets.QSlider(self.page)
        self.manualOffsetBHorizontalSlider.setMaximum(4095)
        self.manualOffsetBHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.manualOffsetBHorizontalSlider.setObjectName("manualOffsetBHorizontalSlider")
        self.horizontalLayout_12.addWidget(self.manualOffsetBHorizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        self.parameterStackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(410, 300, 54, 12))
        self.label.setObjectName("label")
        self.parameterStackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(350, 340, 54, 12))
        self.label_3.setObjectName("label_3")
        self.parameterStackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.ccmTableWidget = QtWidgets.QTableWidget(self.page_4)
        self.ccmTableWidget.setGeometry(QtCore.QRect(20, 90, 421, 151))
        self.ccmTableWidget.setObjectName("ccmTableWidget")
        self.ccmTableWidget.setColumnCount(3)
        self.ccmTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.ccmTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ccmTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ccmTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ccmTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ccmTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ccmTableWidget.setHorizontalHeaderItem(2, item)
        self.parameterStackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.parameterStackedWidget.addWidget(self.page_5)
        self.horizontalLayout_6.addWidget(self.parameterStackedWidget)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.connectIndicatorLabel = QtWidgets.QLabel(self.frame_8)
        self.connectIndicatorLabel.setMinimumSize(QtCore.QSize(50, 50))
        self.connectIndicatorLabel.setMaximumSize(QtCore.QSize(50, 50))
        self.connectIndicatorLabel.setStyleSheet("image: url(:/background/connect_success.png);")
        self.connectIndicatorLabel.setText("")
        self.connectIndicatorLabel.setPixmap(QtGui.QPixmap(":/background/C:/Users/yanke/Desktop/连接成功.png"))
        self.connectIndicatorLabel.setScaledContents(True)
        self.connectIndicatorLabel.setObjectName("connectIndicatorLabel")
        self.verticalLayout_4.addWidget(self.connectIndicatorLabel, 0, QtCore.Qt.AlignHCenter)
        self.readParamPushButton = QtWidgets.QPushButton(self.frame_8)
        self.readParamPushButton.setObjectName("readParamPushButton")
        self.verticalLayout_4.addWidget(self.readParamPushButton)
        self.writeParamPushButton = QtWidgets.QPushButton(self.frame_8)
        self.writeParamPushButton.setObjectName("writeParamPushButton")
        self.verticalLayout_4.addWidget(self.writeParamPushButton)
        self.readAllParamPushButton = QtWidgets.QPushButton(self.frame_8)
        self.readAllParamPushButton.setObjectName("readAllParamPushButton")
        self.verticalLayout_4.addWidget(self.readAllParamPushButton)
        self.writeAllParamPushButton = QtWidgets.QPushButton(self.frame_8)
        self.writeAllParamPushButton.setObjectName("writeAllParamPushButton")
        self.verticalLayout_4.addWidget(self.writeAllParamPushButton)
        self.horizontalLayout_14.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.logTextBrowser = QtWidgets.QTextBrowser(self.frame_5)
        self.logTextBrowser.setObjectName("logTextBrowser")
        self.horizontalLayout_8.addWidget(self.logTextBrowser)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.clearLogButton = QtWidgets.QPushButton(self.frame_6)
        self.clearLogButton.setObjectName("clearLogButton")
        self.verticalLayout_2.addWidget(self.clearLogButton)
        self.expoerLogButton = QtWidgets.QPushButton(self.frame_6)
        self.expoerLogButton.setObjectName("expoerLogButton")
        self.verticalLayout_2.addWidget(self.expoerLogButton)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1618, 26))
        self.menubar.setObjectName("menubar")
        self.menuopen = QtWidgets.QMenu(self.menubar)
        self.menuopen.setObjectName("menuopen")
        self.menuconnect = QtWidgets.QMenu(self.menubar)
        self.menuconnect.setObjectName("menuconnect")
        self.menutools = QtWidgets.QMenu(self.menubar)
        self.menutools.setObjectName("menutools")
        self.menucalibration = QtWidgets.QMenu(self.menubar)
        self.menucalibration.setObjectName("menucalibration")
        self.menucapture = QtWidgets.QMenu(self.menubar)
        self.menucapture.setObjectName("menucapture")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionraw2dng = QtWidgets.QAction(MainWindow)
        self.actionraw2dng.setObjectName("actionraw2dng")
        self.actionconnect_board = QtWidgets.QAction(MainWindow)
        self.actionconnect_board.setObjectName("actionconnect_board")
        self.actiondisconnect_board = QtWidgets.QAction(MainWindow)
        self.actiondisconnect_board.setObjectName("actiondisconnect_board")
        self.actionraw = QtWidgets.QAction(MainWindow)
        self.actionraw.setObjectName("actionraw")
        self.actionhttp_jpg = QtWidgets.QAction(MainWindow)
        self.actionhttp_jpg.setObjectName("actionhttp_jpg")
        self.menuconnect.addAction(self.actionconnect_board)
        self.menuconnect.addAction(self.actiondisconnect_board)
        self.menutools.addAction(self.actionraw2dng)
        self.menucalibration.addAction(self.actionraw)
        self.menucapture.addAction(self.actionhttp_jpg)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menuconnect.menuAction())
        self.menubar.addAction(self.menucapture.menuAction())
        self.menubar.addAction(self.menucalibration.menuAction())
        self.menubar.addAction(self.menutools.menuAction())

        self.retranslateUi(MainWindow)
        self.parameterStackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.algorithmListWidget.isSortingEnabled()
        self.algorithmListWidget.setSortingEnabled(False)
        item = self.algorithmListWidget.item(0)
        item.setText(_translate("MainWindow", "BLC"))
        item = self.algorithmListWidget.item(1)
        item.setText(_translate("MainWindow", "DPC"))
        item = self.algorithmListWidget.item(2)
        item.setText(_translate("MainWindow", "LSC"))
        item = self.algorithmListWidget.item(3)
        item.setText(_translate("MainWindow", "CCM"))
        item = self.algorithmListWidget.item(4)
        item.setText(_translate("MainWindow", "GAMMA"))
        self.algorithmListWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "Manual Offset R"))
        self.label_5.setText(_translate("MainWindow", "Manual Offset Gr"))
        self.label_6.setText(_translate("MainWindow", "Manual Offset Gb"))
        self.label_7.setText(_translate("MainWindow", "Manual Offset B"))
        self.label.setText(_translate("MainWindow", "dpc"))
        self.label_3.setText(_translate("MainWindow", "lsc"))
        item = self.ccmTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "R"))
        item = self.ccmTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "G"))
        item = self.ccmTableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "B"))
        item = self.ccmTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "R"))
        item = self.ccmTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "G"))
        item = self.ccmTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "B"))
        self.readParamPushButton.setText(_translate("MainWindow", "Read"))
        self.writeParamPushButton.setText(_translate("MainWindow", "Write"))
        self.readAllParamPushButton.setText(_translate("MainWindow", "Read all"))
        self.writeAllParamPushButton.setText(_translate("MainWindow", "Write all"))
        self.clearLogButton.setText(_translate("MainWindow", "Clear"))
        self.expoerLogButton.setText(_translate("MainWindow", "Export"))
        self.menuopen.setTitle(_translate("MainWindow", "open"))
        self.menuconnect.setTitle(_translate("MainWindow", "connect"))
        self.menutools.setTitle(_translate("MainWindow", "tools"))
        self.menucalibration.setTitle(_translate("MainWindow", "calibration"))
        self.menucapture.setTitle(_translate("MainWindow", "capture"))
        self.actionraw2dng.setText(_translate("MainWindow", "raw2dng"))
        self.actionconnect_board.setText(_translate("MainWindow", "connect board"))
        self.actiondisconnect_board.setText(_translate("MainWindow", "disconnect board"))
        self.actionraw.setText(_translate("MainWindow", "raw"))
        self.actionhttp_jpg.setText(_translate("MainWindow", "http_jpg"))
import ui.pic_rc
