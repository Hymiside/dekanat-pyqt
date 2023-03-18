from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QWidget, QMainWindow, QDialog, QLabel

from widgets.adminPanel import AdminPanel


class Auth(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Деканат.Плюс")
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setStyleSheet("background-color: #141414")

        self._title = QLabel("Добро пожаловать в Деканат.Плюс")
        self._title.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; margin: 0 0 50px 0; "
                                  "text-align: center;")

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
        self._button.clicked.connect(self._check_auth_data)
        self._button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                   "font-size: 16px; color: #FFFFFF")

        form = QVBoxLayout()
        form.addStretch()
        form.addWidget(self._title, alignment=Qt.AlignmentFlag.AlignHCenter)
        form.addWidget(self._login_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        form.addWidget(self._password_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        form.addWidget(self._button, alignment=Qt.AlignmentFlag.AlignHCenter)
        form.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        form.addStretch()

        container = QWidget()
        container.setLayout(form)

        self.setCentralWidget(container)
        self.showMaximized()

    def _check_auth_data(self):
        # dlg = QDialog(self)
        # dlg.setWindowIcon(QtGui.QIcon("assets/error.ico"))
        # dlg.setWindowTitle("Ошибка")
        # dlg.exec()

        self.admin_panel = AdminPanel()
        self.admin_panel.show()
        self.close()