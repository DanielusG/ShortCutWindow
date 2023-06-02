from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings

class Browser(QMainWindow):
    isVisible = False
    def __init__(self, link: str,geometry: dict,name:str, *args, **kwargs):
        super(Browser, self).__init__(*args, **kwargs)
        self.setWindowTitle(name)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.StrongFocus)
        self.geometry = geometry
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.browser.load(QUrl(link))
        self.window = QWidget()
        self.layout.addWidget(self.browser)
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)
        self.show()
        self.setWindowOpacity(0)
        self.move(geometry["x"],geometry["y"])
        self.resize(geometry["width"],geometry["height"])

    def showBrowser(self):
        print("show")
        self.isVisible = True
        self.raise_()
        self.activateWindow()
        self.setWindowOpacity(1)
        self.setFocus(True)
        
        

    def hideBrowser(self):
        self.isVisible = False
        print("hide")
        self.setWindowOpacity(0)
        self.move(self.geometry["x"],self.geometry["y"])
        self.setFocus(False)
        

    def toggleBrowser(self):
        if self.isVisible:
            self.hideBrowser()
        else:
            self.showBrowser()
        

if __name__ == '__main__':
    import sys
    
    app = QApplication(['', '--no-sandbox'])
    browser = Browser('https://www.google.com')
    sys.exit(app.exec_())