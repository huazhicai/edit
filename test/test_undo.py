# coding:utf-8

import sys

from functools import partial

from PyQt5.QtWidgets import *


class CommandSet(QUndoCommand):
    def __init__(self, displayWidget, origText, text, description):
        super(CommandSet, self).__init__(description)
        self.displayWidget = displayWidget
        self.origText = origText
        self.text = text

    def redo(self):
        self.displayWidget.setText(self.text)

    def undo(self):
        self.displayWidget.setText(self.origText)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.createMenus()

        cWidget = QWidget()
        layout = QVBoxLayout(cWidget)

        helloBtn = QPushButton('Hello')
        worldBtn = QPushButton('World')
        helloBtn.clicked.connect(partial(self.buttonClicked, 'hello'))
        worldBtn.clicked.connect(partial(self.buttonClicked, 'world'))
        self.display = QLabel('')

        layout.addWidget(helloBtn)
        layout.addWidget(worldBtn)
        layout.addWidget(self.display)

        self.setCentralWidget(cWidget)

        self.undoStack = QUndoStack(self)

    def createMenus(self):
        self.undoAction = QAction(
            '&Undo',
            self,
            shortcut='Ctrl+Z',
            statusTip='Undo previous operation',
            triggered=self.undo)
        self.redoAction = QAction(
            '&Redo',
            self,
            shortcut='Ctrl+R',
            statusTip='Redo previous operation',
            triggered=self.redo)

        self.fileMenu = self.menuBar().addMenu('&File')
        self.fileMenu.addAction(self.undoAction)
        self.fileMenu.addAction(self.redoAction)

    def buttonClicked(self, val):
        origText = str(self.display.text())
        commandSet = CommandSet(self.display,
                                origText,
                                val,
                                'set display text')
        self.undoStack.push(commandSet)

    def undo(self):
        self.undoStack.undo()

    def redo(self):
        self.undoStack.redo()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
