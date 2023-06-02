import typing
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
import json
from Browser import Browser
from shortcut_manager import ShortCutManager

class WindowsManager(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowsManager, self).__init__(*args, **kwargs)
        #self.setWindowOpacity(0)
        self.windows = json.load(open("config.json"))
        self.browsers = []
        self.shortcuts = []
        for i in self.windows:
            self.browsers.append(Browser(i["link"],i["geometry"],i["name"]))
            self.shortcuts.append(ShortCutManager(self.browsers[-1].toggleBrowser, i["shortcut"]))
        # add a button to close the app
        self.button = QPushButton('Close', self)
        self.button.clicked.connect(self.close)