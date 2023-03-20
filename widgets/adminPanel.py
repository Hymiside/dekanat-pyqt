from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QWidget, QDialog, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, \
    QCheckBox, QGroupBox, QRadioButton, QGridLayout, QListView, QFontComboBox, QComboBox


from widgets.dialogWindows import createStudent


class AdminPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Деканат.Плюс")
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setStyleSheet("background-color: #141414")

        self._title = QLabel("Панель администратора")
        self._title.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; "
                                  "text-align: center;")
        self._title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self._add_teacher_button = QPushButton("Добавить преподавателя")
        self._add_teacher_button.setFixedSize(350, 40)
        self._add_teacher_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                               "font-size: 16px; color: #FFFFFF")

        self._add_student_button = QPushButton("Добавить студента")
        self._add_student_button.setFixedSize(350, 40)
        self._add_student_button.clicked.connect(self.create_student)
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

        lists = [[23,  "Петров Петр Петрович", "Преподаватель"], [24, "Ардаков Игорь Герасимович", "Студент"], [25, "Донченко Иван Андреевич", "Студент"], [26, "Бирюков Евгений Евгеньевич", "Преподаватель"], [27, "Иванов Иван Иванович", "Преподаватель"], [23,  "Петров Петр Петрович", "Преподаватель"], [24, "Ардаков Игорь Герасимович", "Студент"], [25, "Донченко Иван Андреевич", "Студент"], [26, "Бирюков Евгений Евгеньевич", "Преподаватель"], [27, "Иванов Иван Иванович", "Преподаватель"], [23,  "Петров Петр Петрович", "Преподаватель"], [24, "Ардаков Игорь Герасимович", "Студент"], [25, "Донченко Иван Андреевич", "Студент"], [26, "Бирюков Евгений Евгеньевич", "Преподаватель"], [27, "Иванов Иван Иванович", "Преподаватель"]]
        list_data_users = QVBoxLayout()
        list_data_users.setContentsMargins(0, 60, 0, 0)

        col_button = QVBoxLayout()
        col_fullname = QVBoxLayout()
        col_role = QVBoxLayout()
        for i in lists:
            data_user_l = QHBoxLayout()
            button_delete = QPushButton("Подробнее")
            button_delete.clicked.connect(self.open_card(i[0]))
            button_delete.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; font-size: 13px; "
                                        "color: #FFFFFF; width: 120px; height: 30px; margin-left: 150px;")

            fullname = QLabel(i[1])
            fullname.setStyleSheet("font-size: 15px; color: #FFFFFF;")

            role = QLabel(i[2])
            role.setStyleSheet("font-size: 14px; color: #FFFFFF; margin-left: 80px; font-style: italic;")

            col_button.addWidget(button_delete)
            col_fullname.addWidget(fullname)
            col_role.addWidget(role)

            data_user_l.addStretch()
            data_user_l.addLayout(col_fullname)
            data_user_l.addLayout(col_role)
            data_user_l.addLayout(col_button)
            data_user_l.addStretch()
            data_user_l.setSpacing(15)
            list_data_users.addLayout(data_user_l)
            list_data_users.setAlignment(Qt.AlignmentFlag.AlignLeft)

        choice_l = QHBoxLayout()
        choice_l.addStretch()
        choice_l.addWidget(self._choice_button_all)
        choice_l.addWidget(self._choice_button_students)
        choice_l.addWidget(self._choice_button_teachers)
        choice_l.addStretch()
        choice_l.setContentsMargins(0, 10, 0, 0)

        buttons_l = QHBoxLayout()
        buttons_l.addStretch()
        buttons_l.addWidget(self._add_student_button)
        buttons_l.addWidget(self._add_teacher_button)
        buttons_l.setContentsMargins(0, 35, 0, 0)
        buttons_l.addStretch()

        header = QVBoxLayout()
        header.addWidget(self._title)
        header.addLayout(buttons_l)
        header.addWidget(self._search, alignment=Qt.AlignmentFlag.AlignHCenter)
        header.addLayout(choice_l)

        header.addLayout(list_data_users)

        header.setContentsMargins(0, 80, 0, 0)
        header.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(header)

        self.setMenuWidget(container)
        self.showMaximized()

    def open_card(self, name):
        def card():
            dlg = QDialog(self)
            dlg.setWindowIcon(QtGui.QIcon("assets/error.ico"))
            dlg.setWindowTitle("Ошибка")
            dlg.show()
        return card

    def create_student(self):
        a = createStudent.CreateStudent()
        a.exec()


