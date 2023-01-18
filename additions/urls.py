from pycode_ui.zoomplus_urlsui import *


class UrlsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UrlsWindow, self).__init__()

        self.ui = UiSettingsUrls()
        self.ui.setup_ui(self)

        QtGui.QFontDatabase.addApplicationFont('../assets/fonts/Rubik-Regular.ttf')
