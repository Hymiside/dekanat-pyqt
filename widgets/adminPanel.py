from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QWidget, QDialog, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, \
    QCheckBox, QGroupBox, QRadioButton


class AdminPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Деканат.Плюс")
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setStyleSheet("background-color: #141414")

        self._title = QLabel("Панель администратора")
        self._title.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; "
                                  "text-align: center;")
        # self._title.setMargin(15)
        self._title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self._add_teacher_button = QPushButton("Добавить преподавателя")
        self._add_teacher_button.setFixedSize(350, 40)
        self._add_teacher_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                               "font-size: 16px; color: #FFFFFF")

        self._add_student_button = QPushButton("Добавить студента")
        self._add_student_button.setFixedSize(350, 40)
        self._add_student_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                               "font-size: 16px; color: #FFFFFF")

        self._search = QLineEdit()
        self._search.setFixedSize(700, 60)
        self._search.setContentsMargins(0, 20, 0, 0)
        self._search.setPlaceholderText("Вводите с фамилии")
        self._search.setClearButtonEnabled(True)
        self._search.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                   "padding: 0 0 0 10px;")

        self._choice_button_all = QRadioButton("Все")
        self._choice_button_all.setChecked(True)
        self._choice_button_students = QRadioButton("Студенты")
        self._choice_button_teachers = QRadioButton("Преподаватели")

        choice_l = QHBoxLayout()
        choice_l.addStretch(5)
        choice_l.addWidget(self._choice_button_all)
        choice_l.addWidget(self._choice_button_students)
        choice_l.addWidget(self._choice_button_teachers)
        choice_l.addStretch(9)
        choice_l.setContentsMargins(0, 10, 0, 0)

        buttons_l = QHBoxLayout()
        buttons_l.addStretch()
        buttons_l.addWidget(self._add_student_button, Qt.AlignmentFlag.AlignHCenter)
        buttons_l.addWidget(self._add_teacher_button, Qt.AlignmentFlag.AlignHCenter)
        buttons_l.setContentsMargins(0, 35, 0, 0)
        buttons_l.addStretch()

        header = QVBoxLayout()
        header.addWidget(self._title)
        header.addLayout(buttons_l)
        header.addWidget(self._search, alignment=Qt.AlignmentFlag.AlignHCenter)
        header.addLayout(choice_l)
        header.setContentsMargins(0, 80, 0, 0)
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(header)

        self.setMenuWidget(container)
        self.showMaximized()