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
from additions.create import CreateWindow


class UiZoomPlus(object):
    def __init__(self):
        self.cfg = ZoomPlusConfig()

    def setup_ui(self, window):
        window.setObjectName("ZoomPlus")
        window.resize(400, 700)
        window.setMinimumSize(QtCore.QSize(400, 700))
        window.setMaximumSize(QtCore.QSize(400, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Ryzen\PycharmProjects\zoomplus\icons\favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet("""QMainWindow {
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
        QPushButton: pressed {
        background-color: #fa4244;
        }""")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        for e in self.cfg.main_buttons:
            if not self.cfg.check_hide(e.split('_')[-1]):
                setattr(self, e, ButtonsEvent(self.centralwidget))
                getattr(self, e).setObjectName(e)
                self.verticalLayout.addWidget(getattr(self, e))
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
        self.create = QtGui.QAction(window)
        self.create.setObjectName('create_conf')
        self.menu.addAction(self.open_urls)
        self.menu.addAction(self.open_names)
        self.menu.addAction(self.create)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslate_ui(window)

        urls = UrlsWindow()
        names = NamesWindow()
        create = CreateWindow()

        self.open_urls.triggered.connect(lambda: urls.show())  # type: ignore
        self.open_names.triggered.connect(lambda: names.show())  # type: ignore
        self.create.triggered.connect(lambda: create.show())  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("ZoomPlus", "ZoomPlus"))

        for btn in self.cfg.main_buttons:
            if not self.cfg.check_hide(btn.split("_")[-1]):
                getattr(self, btn).clicked.connect(lambda: self.cfg.open_url_conf(self.connect(window)))

        for ind, btn in enumerate(self.cfg.main_buttons):
            if not self.cfg.check_hide(btn.split("_")[-1]):
                getattr(self, btn).setText(_translate("ZoomPlus", self.cfg.get_name_conf(ind)))

        for btn, val in self.cfg.main_shortcut.items():
            if not self.cfg.check_hide(btn.split('_')[-1]):
                getattr(self, btn).setShortcut(_translate("ZoomPlus", val))

        self.menu.setTitle(_translate("ZoomPlus", "Настройки"))
        self.open_urls.setText(_translate("ZoomPlus", "Настроить ссылки"))
        self.open_urls.setShortcut(_translate("ZoomPlus", "Ctrl+U"))
        self.open_names.setText(_translate("ZoomPlus", "Настроить названия конференций"))
        self.open_names.setShortcut(_translate("ZoomPlus", "Ctrl+N"))
        self.create.setText(_translate("ZoomPlus", 'Создать'))
        self.create.setShortcut(_translate("ZoomPlus", "Ctrl+M"))

    def connect(self, window):
        btn = window.sender().objectName()
        if btn in self.cfg.main_buttons:
            return int(btn.split('_')[-1])


class ButtonsEvent(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cfg = ZoomPlusConfig()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        button = event.button()
        box = QtWidgets.QMessageBox()
        if button == QtCore.Qt.MouseButton.RightButton:
            window = QtWidgets.QWidget()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(r"C:\Users\Ryzen\PycharmProjects\zoomplus\icons\favicon.ico"),
                           QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            window.setWindowIcon(icon)
            checkbox = box.information(window,
                                       "Удаление конференции",
                                       "Вы действительно хотите удалить конференцию?",
                                       box.StandardButton.Ok | box.StandardButton.Cancel)
            if checkbox == 1024:
                self.remove_button()
        return QtWidgets.QPushButton.mousePressEvent(self, event)

    def remove_button(self):
        self.hide()
        data_read = [e.get("name_conf") for e in self.cfg.read_data_conf()]
        ind = data_read.index(self.text())
        self.cfg.set_hide_button(ind)
