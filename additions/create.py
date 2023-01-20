from pycode_ui.zoomplus_createui import *


class CreateWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreateWindow, self).__init__()

        self.ui = UiCreate()
        self.ui.setup_ui(self)

        QtGui.QFontDatabase.addApplicationFont('../assets/fonts/Rubik-Regular.ttf')
