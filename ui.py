import os
import sys

from PySide2 import QtWidgets as qtw
from PySide2 import QtCore as qtc
from PySide2 import QtGui as qtg


import work_log as wl

TOPICS = wl.get_topic_dict()

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
    # Tab for viewing log list and reading a selected log entry
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass


class WLEntryWidget(qtw.QTabWidget):
    # Tab for adding a new entry to the log
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
        save_button.clicked.connect(self.save_entry)
        self.select_topic_combo = TopicListWidget()


        button_layout = qtw.QHBoxLayout()
        button_layout.addWidget(clear_button)
        button_layout.addWidget(save_button)

        textbox_layout = qtw.QHBoxLayout()
        textbox_layout.setAlignment(qtc.Qt.AlignTop)
        textbox_layout.addWidget(self.select_topic_combo)
        textbox_layout.addWidget(self.entry_texbox)
        entry_layout.addLayout(button_layout)
        entry_layout.addLayout(textbox_layout)


        self.setLayout(entry_layout)

    def clear_entry(self):
        self.entry_texbox.clear()

    def get_topics(self):
        print('getting topics')

    def save_entry(self):
        index = TOPICS[self.select_topic_combo.currentText()]
        text = self.entry_texbox.toPlainText()
        wl.add_log_entry(index, text)


class TopicListWidget(qtw.QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.topics_dict = TOPICS
        self.addItems(self.topics_dict.keys())
        self.setFixedWidth(200)




if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())