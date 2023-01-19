# Form implementation generated from reading ui file '.\zoomplusui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

__all__ = ['UiZoomPlus', 'QtCore', 'QtWidgets', 'QtGui']

from PyQt6 import QtCore, QtGui, QtWidgets

import qrc.files  # type: ignore
from config import ZoomPlusConfig
from additions.urls import UrlsWindow
from additions.names import NamesWindow


class UiZoomPlus(object):
    def setup_ui(self, window):
        window.setObjectName("ZoomPlus")
        window.resize(400, 700)
        window.setMinimumSize(QtCore.QSize(400, 700))
        window.setMaximumSize(QtCore.QSize(400, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet("QMainWindow {\n"
                             "    background-color: #22222e;\n"
                             "}\n"
                             "\n"
                             "QPushButton {\n"
                             "    color: white;\n"
                             "    font-family: Rubik, sans-serif;\n"
                             "    background-color: #fb5b5d;\n"
                             "    border-radius: 6px;\n"
                             "    font-size: 16pt;\n"
                             "    font-weight: 600;\n"
                             "}\n"
                             "\n"
                             "QPushButton:pressed {\n"
                             "    background-color: #fa4244;\n"
                             "}")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setObjectName("btn_0")
        self.verticalLayout.addWidget(self.btn_0)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setObjectName("btn_1")
        self.verticalLayout.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setObjectName("btn_2")
        self.verticalLayout.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setObjectName("btn_3")
        self.verticalLayout.addWidget(self.btn_3)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setObjectName("btn_4")
        self.verticalLayout.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setObjectName("btn_5")
        self.verticalLayout.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setObjectName("btn_6")
        self.verticalLayout.addWidget(self.btn_6)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setObjectName("btn_7")
        self.verticalLayout.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setObjectName("btn_8")
        self.verticalLayout.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setObjectName("btn_9")
        self.verticalLayout.addWidget(self.btn_9)
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        window.setMenuBar(self.menubar)
        self.open_urls = QtGui.QAction(window)
        self.open_urls.setObjectName("open_urls")
        self.open_names = QtGui.QAction(window)
        self.open_names.setObjectName("open_names")
        self.menu.addAction(self.open_urls)
        self.menu.addAction(self.open_names)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslate_ui(window)

        urls = UrlsWindow()
        names = NamesWindow()

        self.open_urls.triggered.connect(lambda: urls.show())  # type: ignore
        self.open_names.triggered.connect(lambda: names.show())  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        self.cfg = ZoomPlusConfig()
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("ZoomPlus", "ZoomPlus"))

        for btn in self.cfg.main_buttons:
            getattr(self, btn).clicked.connect(lambda: self.cfg.open_url_conf(self.connect(window)))

        for ind, val in enumerate(self.cfg.main_buttons):
            getattr(self, val).setText(_translate("ZoomPlus", self.cfg.get_name_conf(ind)))

        for btn, val in self.cfg.main_shortcut.items():
            getattr(self, btn).setShortcut(_translate("ZoomPlus", val))

        self.menu.setTitle(_translate("ZoomPlus", "Настройки"))
        self.open_urls.setText(_translate("ZoomPlus", "Настроить ссылки"))
        self.open_urls.setStatusTip(_translate("ZoomPlus", "Настройка ссылок конференций"))
        self.open_urls.setShortcut(_translate("ZoomPlus", "Ctrl+U"))
        self.open_names.setText(_translate("ZoomPlus", "Настроить названия конференций"))
        self.open_names.setStatusTip(_translate("ZoomPlus", "Настройка названий конференций"))
        self.open_names.setShortcut(_translate("ZoomPlus", "Ctrl+N"))

    def connect(self, window):
        btn = window.sender().objectName()
        if btn in self.cfg.main_buttons:
            return int(btn.split('_')[-1])
