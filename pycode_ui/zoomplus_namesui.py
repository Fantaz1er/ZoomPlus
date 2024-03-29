# Form implementation generated from reading ui file '.\zoomplus_namesui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing
from PyQt6 import QtCore, QtGui, QtWidgets

import qrc.files  # type: ignore
from config import ZoomPlusConfig


class UiSettingsNames(object):
    def __init__(self):
        self.cfg = ZoomPlusConfig()

    def setup_ui(self, window):
        window.setObjectName("Names")
        window.resize(270, 510)
        window.setMinimumSize(QtCore.QSize(270, 510))
        window.setMaximumSize(QtCore.QSize(270, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Ryzen\PycharmProjects\zoomplus\icons\favicon.ico"),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        window.setWindowIcon(icon)
        window.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        window.setStyleSheet("""QMainWindow {
    font-family: Rubik, sans-serif;
    background-color: #22222e;
}

QLineEdit {
    font-family: Rubik, sans-serif;
    background-color: #22222e;
    border: 2px solid #f66867;
    border-radius: 6px;
    color: white;
    font-size: 12pt;
    font-weight: 600;
}

QPushButton {
    color: white;
    font-family: Rubik, sans-serif;
    background-color: #fb5b5d;
    border-radius: 6px;
    font-size: 14pt;
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
        self.btn_entry = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entry.setGeometry(QtCore.QRect(95, 480, 75, 20))
        self.btn_entry.setObjectName("pushButton")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")

        for ind, le in enumerate(self.cfg.main_le):
            if not self.cfg.check_hide(ind):
                setattr(self, le, QtWidgets.QLineEdit(self.centralwidget))
                getattr(self, le).setMinimumSize(QtCore.QSize(250, 25))
                getattr(self, le).setMaximumSize(QtCore.QSize(250, 25))
                getattr(self, le).setMaxLength(16)
                getattr(self, le).setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                getattr(self, le).setObjectName("le_0")
                self.verticalLayout.addWidget(getattr(self, le))

        self.verticalLayout_2.addLayout(self.verticalLayout)
        window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(window)

        self.btn_entry.clicked.connect(self.change)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        self.btn_entry.setText(_translate("Names", 'Save'))
        self.btn_entry.setShortcut(_translate('Names', "Return"))
        for ind, le in enumerate(self.cfg.main_le):
            if not self.cfg.check_hide(ind):
                getattr(self, le).setPlaceholderText(self.cfg.get_name_conf(ind))
        window.setWindowTitle(_translate("Names", "Настройка названий конференций"))

    def change(self) -> None:
        for ind, le in enumerate(self.cfg.main_le):
            if not self.cfg.check_hide(ind):
                text = getattr(self, le).text().title()
                if text:
                    self.cfg.set_name_conf(text, ind)
