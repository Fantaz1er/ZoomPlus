from sys import argv, exit
from pycode_ui.zoomplusui import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = UiZoomPlus()
        self.ui.setup_ui(self)

        QtGui.QFontDatabase.addApplicationFont('assets/fonts/Rubik-Bold.ttf')


if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
