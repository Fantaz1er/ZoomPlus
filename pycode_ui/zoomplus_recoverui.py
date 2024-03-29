# Form implementation generated from reading ui file '.\zoomplus_recoverui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

import qrc.files  # type: ignore
from config import ZoomPlusConfig


class UiRecover(object):
    def __init__(self):
        self.cfg = ZoomPlusConfig()
        self.modal_windows = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Ryzen\PycharmProjects\zoomplus\icons\favicon.ico"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.modal_windows.setWindowIcon(icon)

    def setup_ui(self, window):
        window.setObjectName("Recover")
        window.resize(250, 320)
        window.setMinimumSize(QtCore.QSize(250, 320))
        window.setMaximumSize(QtCore.QSize(250, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Ryzen\PycharmProjects\zoomplus\icons\favicon.ico"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet("""QWidget {
    background-color: #22222e;
    border: none;
}

QMainWindow {
    font-family: Rubik, sans-serif;
    background-color: #22222e;
}

QPushButton {
    color: white;
    font-family: Rubik, sans-serif;
    background-color: #fb5b5d;
    border-radius: 6px;
    font-size: 16pt;
    font-weight: 600;
}

QPushButton:pressed {
    background-color: #fa4244;
}

QLabel {
    font-family: Rubik, sans-serif;
    color: white;
    font-size: 10pt;
    font-weight: 600;
}""")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 225, 310))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.empty = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.empty.setObjectName('empty')

        self.buttons = []

        if self.cfg.get_count_actual_hidden:
            for i, e in enumerate(self.cfg.read_recovers_conf()):
                setattr(self, f'btn_{i}', QtWidgets.QPushButton(self.scrollAreaWidgetContents))
                getattr(self, f'btn_{i}').setObjectName(f'btn_{i}')
                self.verticalLayout.addWidget(getattr(self, f'btn_{i}'))
                getattr(self, f'btn_{i}').setText(e['name_conf'])
                self.buttons.append(f'btn_{i}')
        else:
            self.empty.setText('Пусто')
            self.verticalLayout.addWidget(self.empty, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea)
        window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(window)

        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Recover", "Восстановление конференций"))

        for btn in self.buttons:
            getattr(self, btn).clicked.connect(lambda: self.recover(window))

    def recover(self, window, ind: int = None, ind_recover: int = None) -> None:
        if self.cfg.get_count_actual_buttons < self.cfg.limit_buttons:
            name_conf = window.sender().text()
            data = self.cfg.read_data_conf()
            recover_data = self.cfg.read_recovers_conf()
            for e in data:
                if e['name_conf'] == name_conf:
                    ind = data.index(e)
            for e in recover_data:
                if e['name_conf'] == name_conf:
                    ind_recover = recover_data.index(e)
            if ind is not None and ind_recover is not None:
                self.cfg.set_show_button(ind)
                self.cfg.delete_recover(ind_recover)
        else:
            QtWidgets.QMessageBox.warning(self.modal_windows, "Лимит", f'Максимальное количество конференций: '
                                                                       f'{self.cfg.limit_buttons}')
