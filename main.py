from Browser import Browser
from PyQt5.QtWidgets import QApplication
from shortcut_manager import ShortCutManager
from windowsManager import WindowsManager
app = QApplication(['', '--no-sandbox']) # --no-sandbox is for linux
browser = WindowsManager()


if __name__ == '__main__':
    browser.show()
    app.exec_() 