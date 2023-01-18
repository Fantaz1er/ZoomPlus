from pycode_ui.zoomplus_namesui import *


class NamesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(NamesWindow, self).__init__()

        self.ui = UiSettingsNames()
        self.ui.setup_ui(self)

        QtGui.QFontDatabase.addApplicationFont('../assets/fonts/Rubik-Regular.ttf')
