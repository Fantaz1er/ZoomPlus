from sys import argv, exit
from pycode_ui.zoomplusui import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = UiZoomPlus()
        self.ui.setup_ui(self)

        QtGui.QFontDatabase.addApplicationFont('assets/fonts/Rubik-Regular.ttf')


if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    window = Window()
    window.show()
    exit(app.exec())
