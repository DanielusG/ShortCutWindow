from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings

class Browser(QMainWindow):
    isVisible = False
    def __init__(self, link: str,geometry: dict,name:str, *args, **kwargs):
        super(Browser, self).__init__(*args, **kwargs)
        #self.titleBar.raise_()
        self.setWindowTitle(name)
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.geometry = geometry
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.browser.load(QUrl(link))
        #self.browser.show()
        self.window = QWidget()
        self.layout.addWidget(self.browser)
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)
        #self.setCentralWidget(self.window)
        self.show()
        self.setWindowOpacity(0)
        self.move(geometry["x"],geometry["y"])
        self.resize(geometry["width"],geometry["height"])
        # hide in taskbar
        #self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    def showBrowser(self):
        print("show")
        self.isVisible = True
        #set window opacity to 1
        self.setWindowOpacity(1)
        
        #ripristina la finestra
        self.showNormal()

        #ridiamo il focus alla finestra
        self.activateWindow()

    def hideBrowser(self):
        self.isVisible = False
        print("hide")
        #set window opacity to 0
        self.setWindowOpacity(0)
        # riduco ad icona la finestra
        #self.showMinimized()
        self.move(self.geometry["x"],self.geometry["y"])

        
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