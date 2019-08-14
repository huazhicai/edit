#coding:utf-8

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		scene = QGraphicsScene()
		scene.setSceneRect(QRectF(-2000,-2000,4000,4000))
		rect = QGraphicsRectItem(QRectF(-50,-50,100,100))
		scene.addItem(rect)
		rect.setPos(0,0)

		view = QGraphicsView(scene)

		label = QLabel()
		label.setText('<h1>Hello</h1>')

		mainWidget = QWidget()
		layout = QGridLayout(mainWidget)
		layout.addWidget(view,0,0,5,5)
		layout.addWidget(label,0,0,1,3)

		self.setCentralWidget(mainWidget)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	app.exec_()

