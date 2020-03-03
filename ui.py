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

        # Set up base tab widget
        tab_controller = qtw.QTabWidget()

        view_log_tab = EntryReaderWidget()
        entry_tab = WLEntryWidget()

        # Add layouts to TabWidget
        tab_controller.addTab(view_log_tab, 'Work Log Reader')
        tab_controller.addTab(entry_tab, 'Work Log Entry')


        layout_frame = qtw.QHBoxLayout()
        layout_frame.addWidget(tab_controller)

        self.setLayout(layout_frame)


class EntryReaderWidget(qtw.QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass


class WLEntryWidget(qtw.QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        entry_layout = qtw.QVBoxLayout()
        
        save_button = qtw.QPushButton('Save') #call db logic
        clear_button = qtw.QPushButton('Clear')
        self.entry_texbox = qtw.QTextEdit()
        self.entry_texbox.setMaximumWidth(600)
        self.entry_texbox.setFontPointSize(10)
        self.entry_texbox.setAlignment(qtc.Qt.AlignLeft)
        save_button.setFixedWidth(150)
        clear_button.setFixedWidth(150)
        clear_button.clicked.connect(self.clear_entry)

        button_layout = qtw.QHBoxLayout()
        button_layout.addWidget(clear_button)
        button_layout.addWidget(save_button)

        entry_layout.addLayout(button_layout)
        entry_layout.addWidget(self.entry_texbox)

        self.setLayout(entry_layout)


def clear_entry(self):
    self.entry_textbox.clear()




if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())