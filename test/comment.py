# coding:utf-8
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QMainWindow, QGraphicsTextItem, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, \
    QApplication


class CommentWindow(QMainWindow):
    def __init__(self):
        super(CommentWindow, self).__init__()

        item = QGraphicsTextItem('Data')
        item.setTextInteractionFlags(Qt.TextEditable)

        scene = QGraphicsScene()
        scene.addItem(item)

        view = QGraphicsView(scene)
        layout = QVBoxLayout()
        layout.addWidget(view)

        self.main_widget = QWidget()
        self.main_widget.setLayout(layout)

        self.setCentralWidget(self.main_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CommentWindow()
    w.show()
    app.exec_()
