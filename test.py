


import sys
from PyQt5 import QtWidgets
from ui.ui_main_new import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的应用程序
    mainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()    # ui是你创建的ui类的实例化对象，这里调用的便是刚才生成的register.py中的Ui_MainWindow类
    ui.setupUi(mainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    mainWindow.show()   # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec())    # 使用exit()或者点击关闭按钮退出QApplication
