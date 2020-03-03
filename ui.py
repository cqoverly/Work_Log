import os
import sys

from PySide2 import QtWidgets as qtw
from PySide2 import QtCore as qtc
from PySide2 import QtGui as qtg

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        exitAction = qtw.QAction( ' &Exit', self)
        exitAction.triggered.connect(app.quit)

        menubar = qtw.QMenuBar()
        fileMenu = menubar.addMenu('&Testmenu')
        fileMenu.addAction(exitAction)

        main_frame = MainManager()
        self.setCentralWidget(main_frame)
        self.setWindowTitle('Work Log')
        self.setFixedSize(800, 600)

        self.show()


class MainManager(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)







if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())