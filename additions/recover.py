from pycode_ui.zoomplus_recoverui import *


class RecoverWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UiRecover()
        self.ui.setup_ui(self)

        QtGui.QFontDatabase.addApplicationFont('../assets/fonts/Rubik-Regular.ttf')
