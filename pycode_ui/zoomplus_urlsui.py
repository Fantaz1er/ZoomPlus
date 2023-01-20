# Form implementation generated from reading ui file '.\zoomplus_urlsui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

__all__ = ['UiSettingsUrls', 'QtCore', 'QtWidgets', 'QtGui']

from PyQt6 import QtCore, QtGui, QtWidgets

from config import ZoomPlusConfig
import qrc.files  # type: ignore


class UiSettingsUrls(object):
    def __init__(self):
        self.cfg = ZoomPlusConfig()

    def setup_ui(self, window):
        window.setObjectName("ZoomPlus")
        window.resize(270, 430)
        window.setMinimumSize(QtCore.QSize(270, 430))
        window.setMaximumSize(QtCore.QSize(270, 430))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Ryzen\PycharmProjects\zoomplus\icons\favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet("QMainWindow {\n"
                             "    background-color: #22222e;\n"
                             "    font-family: Rubik, sans-serif;\n"
                             "    color: white;\n"
                             "    font-size: 8pt;\n"
                             "    font-weight: 600;\n"
                             "}\n"
                             "\n"
                             "QLabel {\n"
                             "    font-family: Rubik, sans-serif;\n"
                             "    color: white;\n"
                             "    font-size: 10pt;\n"
                             "    font-weight: 600;\n"
                             "}\n"
                             "\n"
                             "QLineEdit {\n"
                             "    font-family: Rubik, sans-serif;\n"
                             "    background-color: #22222e;\n"
                             "    border: 2px solid #f66867;\n"
                             "    font-size: 10pt;\n"
                             "    border-radius: 6px;\n"
                             "    color: white;\n"
                             "    font-size: 8pt;\n"
                             "    font-weight: 600;\n"
                             "}"
                             "\n"
                             "QPushButton {\n"
                             "    color: white;\n"
                             "    background-color: #fb5b5d;\n"
                             "    border-radius: 10px;\n"
                             "}\n"
                             "\n"
                             "QPushButton:pressed {\n"
                             "    background-color: #fa4244;\n"
                             "}")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_entry = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entry.setGeometry(QtCore.QRect(95, 400, 75, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setBold(True)
        font.setWeight(75)
        self.btn_entry.setFont(font)
        self.btn_entry.setObjectName("pushButton")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(11)
        self.formLayout.setVerticalSpacing(19)
        self.formLayout.setObjectName("formLayout")
        self.lbl_0 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_0.setObjectName("lbl_0")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_0)
        self.le_0 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_0.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_0.setMaxLength(125)
        self.le_0.setObjectName("le_0")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_0)
        self.lbl_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_1.setObjectName("lbl_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_1)
        self.le_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_1.setMaxLength(125)
        self.le_1.setObjectName("le_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_1)
        self.lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_2.setObjectName("lbl_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_2)
        self.le_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_2.setMaxLength(125)
        self.le_2.setObjectName("le_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_2)
        self.lbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_3.setObjectName("lbl_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_3)
        self.le_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_3.setMaxLength(125)
        self.le_3.setObjectName("le_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_3)
        self.lbl_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_4.setObjectName("lbl_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_4)
        self.le_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_4.setMaxLength(125)
        self.le_4.setObjectName("le_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_4)
        self.lbl_5 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_5.setObjectName("lbl_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_5)
        self.le_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_5.setMaxLength(125)
        self.le_5.setObjectName("le_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_5)
        self.lbl_6 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_6.setObjectName("lbl_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_6)
        self.le_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_6.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_6.setMaxLength(125)
        self.le_6.setObjectName("le_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_6)
        self.lbl_7 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_7.setObjectName("lbl_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_7)
        self.le_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_7.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_7.setMaxLength(125)
        self.le_7.setObjectName("le_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_7)
        self.lbl_8 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_8.setObjectName("lbl_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_8)
        self.le_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_8.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_8.setMaxLength(125)
        self.le_8.setObjectName("le_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_8)
        self.lbl_9 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_9.setObjectName("lbl_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lbl_9)
        self.le_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_9.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_9.setMaxLength(125)
        self.le_9.setObjectName("le_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.le_9)
        self.verticalLayout.addLayout(self.formLayout)
        window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(window)

        self.btn_entry.clicked.connect(self.change)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("ZoomPlus", "Настройка ссылок конференций"))
        self.btn_entry.setText(_translate("Zoom Plus", 'Save'))
        self.btn_entry.setShortcut(_translate('Zoom Plus', "Return"))
        for ind, le in enumerate(self.cfg.main_le):
            getattr(self, le).setPlaceholderText(self.cfg.get_url_conf(ind))

        for ind, lbl in enumerate(self.cfg.main_lbl):
            getattr(self, lbl).setText(_translate("ZoomPlus", self.cfg.get_name_conf(ind)))

    def change(self):
        for ind, le in enumerate(self.cfg.main_le):
            text = getattr(self, le).text()
            if text:
                self.cfg.set_url_conf(text, ind)
