from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QWidget, QMainWindow, QDialog, QLabel, QHBoxLayout

from widgets.adminPanel import AdminPanel


class Auth(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Деканат.Плюс")
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setStyleSheet("background-color: #141414")

        self._title = QLabel("Добро пожаловать в Деканат.Плюс")
        self._title.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; "
                                  "text-align: center;")
        self._title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self._login_input = QLineEdit()
        self._login_input.setFixedSize(350, 50)
        self._login_input.setPlaceholderText("Логин")
        self._login_input.setClearButtonEnabled(True)
        self._login_input.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; padding: 0 0 0 "
                                        "10px; font-size: 13px;")

        self._password_input = QLineEdit()
        self._password_input.setFixedSize(350, 50)
        self._password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self._password_input.setPlaceholderText("Пароль")
        self._password_input.setClearButtonEnabled(True)
        self._password_input.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; padding: 0 0"
                                           " 0 10px; font-size: 13px;")

        self._button = QPushButton("Войти")
        self._button.setFixedSize(350, 50)
        self._button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self._button.clicked.connect(self._check_auth_data)
        self._button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                   "font-size: 16px; color: #FFFFFF;")

        title_l = QHBoxLayout()
        title_l.addWidget(self._title)

        form = QVBoxLayout()
        form.addStretch()
        form.addWidget(self._login_input)
        form.addSpacing(5)
        form.addWidget(self._password_input)
        form.addSpacing(20)
        form.addWidget(self._button)
        form.addStretch()
        form.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        login = QVBoxLayout()
        login.addStretch()
        login.addWidget(self._title)
        login.addLayout(form)
        login.addStretch()

        container = QWidget()
        container.setLayout(login)

        self.setCentralWidget(container)
        self.showMaximized()

    def _check_auth_data(self):
        self.admin_panel = AdminPanel()
        self.admin_panel.show()
        self.close()