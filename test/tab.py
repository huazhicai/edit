# coding:utf-8


import sys

from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Tab窗口')

        self.tabWidget = QTabWidget()
        self.tabWidget.setSizePolicy(QSizePolicy.Preferred,
                                     QSizePolicy.Ignored)
        self.tabWidget.setMovable(True)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)
        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5,5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()
        textEdit.setPlainText("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n"
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n"
                              "How I wonder what you are!\n")
        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5,5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.tabWidget.addTab(tab1, '&Table')
        self.tabWidget.addTab(tab2, 'Text &Edit')

        self.setCentralWidget(self.tabWidget)


def test():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()


if __name__ == '__main__':
    test()
