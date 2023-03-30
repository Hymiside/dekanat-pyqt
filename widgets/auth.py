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

        self.title_text = QLabel("Добро пожаловать в Деканат.Плюс")
        self.title_text.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; "
                                      "text-align: center;")
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.login_input = QLineEdit()
        self.login_input.setFixedSize(350, 50)
        self.login_input.setPlaceholderText("Логин")
        self.login_input.setClearButtonEnabled(True)
        self.login_input.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; padding: 0 0 0 "
                                       "10px; font-size: 13px;")

        self.password_input = QLineEdit()
        self.password_input.setFixedSize(350, 50)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; padding: 0 0"
                                          " 0 10px; font-size: 13px;")

        self.login_button = QPushButton("Войти")
        self.login_button.setFixedSize(350, 50)
        self.login_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_button.clicked.connect(self._check_auth_data)
        self.login_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                        "font-size: 16px; color: #FFFFFF;")

        title_layout = QHBoxLayout()
        title_layout.addWidget(self.title_text)

        login_form_layout = QVBoxLayout()
        login_form_layout.addStretch()
        login_form_layout.addWidget(self.login_input)
        login_form_layout.addSpacing(5)
        login_form_layout.addWidget(self.password_input)
        login_form_layout.addSpacing(20)
        login_form_layout.addWidget(self.login_button)
        login_form_layout.addStretch()
        login_form_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        widget_layout = QVBoxLayout()
        widget_layout.addStretch()
        widget_layout.addWidget(self.title_text)
        widget_layout.addLayout(login_form_layout)
        widget_layout.addStretch()

        container = QWidget()
        container.setLayout(widget_layout)

        self.setCentralWidget(container)
        self.showMaximized()

    def _check_auth_data(self):
        self.admin_panel = AdminPanel()
        self.admin_panel.show()
        self.close()