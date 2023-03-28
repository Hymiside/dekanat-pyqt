import uuid
from typing import List, NamedTuple

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QDialog, QDateEdit, QPushButton

from service import service


class StudentData(NamedTuple):
    user_id: str
    # TODO


class CreateTeacher(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setWindowTitle("Деканат.Плюс")
        self.setStyleSheet("background-color: #141414")
        self.setFixedSize(850, 600)

        left_column = QVBoxLayout()
        right_column = QVBoxLayout()
        get_student_info = QHBoxLayout()
        get_student_info.setContentsMargins(0, 50, 0, 0)

        title_dialog = QLabel("Создание нового преподавателя")
        title_dialog.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF;")
        title_dialog.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.last_n = QLineEdit()
        self.last_n.setPlaceholderText("Фамилия")
        self.last_n.setFixedSize(250, 45)
        self.last_n.setClearButtonEnabled(True)
        self.last_n.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                  "padding: 0 0 0 10px; margin-right: 5px;")
        self.first_n = QLineEdit()
        self.first_n.setPlaceholderText("Имя")
        self.first_n.setFixedSize(250, 45)
        self.first_n.setClearButtonEnabled(True)
        self.first_n.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                   "padding: 0 0 0 10px; margin-right: 5px;")
        self.middle_n = QLineEdit()
        self.middle_n.setPlaceholderText("Отчество")
        self.middle_n.setFixedSize(250, 45)
        self.middle_n.setClearButtonEnabled(True)
        self.middle_n.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                    "padding: 0 0 0 10px;")
        name_form_layout = QHBoxLayout()
        name_form_layout.addStretch()
        name_form_layout.addWidget(self.last_n)
        name_form_layout.addWidget(self.first_n)
        name_form_layout.addWidget(self.middle_n)
        name_form_layout.addStretch()
        name_form_layout.setContentsMargins(0, 50, 0, 0)


        self.title_form_edu = QLabel("Кафедра:")
        self.title_form_edu.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.choice_form_edu = QComboBox()
        self.choice_form_edu.addItems(["МОВС", "ВМ", "КМБ", "ИТ", "ВЭМ", "ПМИ", "ФМ"])
        self.choice_form_edu.setFixedSize(200, 30)
        self.choice_form_edu.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                           "font-size: 14px; padding: 0 0 0 10px;")
        form_edu_layout = QHBoxLayout()
        form_edu_layout.addWidget(self.title_form_edu)
        form_edu_layout.addWidget(self.choice_form_edu)


        self.title_number_course = QLabel("Категория:")
        self.title_number_course.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.number_course = QComboBox()
        self.number_course.addItems(["МОВС", "ВМ", "КМБ", "ИТ", "ВЭМ", "ПМИ", "ФМ"])
        self.number_course.setFixedSize(200, 30)
        self.number_course.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                         "font-size: 14px; padding: 0 0 0 10px;")
        number_course_layout = QHBoxLayout()
        number_course_layout.addWidget(self.title_number_course)
        number_course_layout.addWidget(self.number_course)

        left_column.addLayout(form_edu_layout)
        left_column.addSpacing(10)
        right_column.addLayout(number_course_layout)
        right_column.addSpacing(10)

        get_student_info.addStretch()
        get_student_info.addLayout(left_column)
        get_student_info.addSpacing(160)
        get_student_info.addLayout(right_column)
        get_student_info.addStretch()


        title_birthday = QLabel("Дата рождения:")
        title_birthday.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.birthday = QDateEdit(calendarPopup=True)
        self.birthday.setFixedSize(200, 30)
        self.birthday.setStyleSheet("background-color: #424242; color: #A2A2A2; border-radius: 5px;"
                                    "font-size: 14px; padding: 0 0 0 10px; font-weight: medium;")
        birthday_layout = QHBoxLayout()
        birthday_layout.addWidget(title_birthday)
        birthday_layout.addWidget(self.birthday)


        title_passport_id = QLabel("Email:")
        title_passport_id.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.passport_id = QLineEdit()
        self.passport_id.setFixedSize(200, 35)
        self.passport_id.setPlaceholderText("example@info.com")
        self.passport_id.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                       "font-size: 14px; padding: 0 0 0 10px; margin-right: 5px;")
        passport_id_layout = QHBoxLayout()
        passport_id_layout.addWidget(title_passport_id)
        passport_id_layout.addWidget(self.passport_id)

        left_column.addLayout(birthday_layout)
        left_column.addSpacing(10)
        right_column.addLayout(passport_id_layout)
        right_column.addSpacing(10)

        get_student_info.addLayout(left_column)
        get_student_info.addLayout(right_column)


        login_student_title = QLabel("Логин")
        login_student_title.setStyleSheet("font-size: 13px; color: #FFFFFF;")
        self.login_student = QLineEdit()
        self.login_student.setPlaceholderText("Логин")
        self.login_student.setFixedSize(375, 45)
        self.login_student.setText(f"teacher{str(uuid.uuid4())[:8]}")
        self.login_student.setDisabled(True)
        self.login_student.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                         "font-size: 14px; padding: 0 0 0 10px; margin-right: 5px;")

        login_input_layout = QVBoxLayout()
        login_input_layout.addStretch()
        login_input_layout.addWidget(login_student_title, alignment=Qt.AlignmentFlag.AlignLeft)
        login_input_layout.addWidget(self.login_student)
        login_input_layout.addStretch()


        password_student_title = QLabel("Пароль")
        password_student_title.setStyleSheet("font-size: 13px; color: #FFFFFF;")
        self.password_student = QLineEdit()
        self.password_student.setFixedSize(375, 45)
        self.password_student.setText(f"{str(uuid.uuid4())[:3]}{str(uuid.uuid4())[:4]}{str(uuid.uuid4())[:4]}")
        self.password_student.setDisabled(True)
        self.password_student.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                            "font-size: 14px; padding: 0 0 0 10px; margin-right: 5px;")
        password_input_layout = QVBoxLayout()
        password_input_layout.addStretch()
        password_input_layout.addWidget(password_student_title, alignment=Qt.AlignmentFlag.AlignLeft)
        password_input_layout.addWidget(self.password_student)
        password_input_layout.addStretch()

        auth_form_layout = QHBoxLayout()
        auth_form_layout.addStretch()
        auth_form_layout.addLayout(login_input_layout)
        auth_form_layout.addLayout(password_input_layout)
        auth_form_layout.addStretch()
        auth_form_layout.setContentsMargins(0, 25, 0, 0)


        save_data_button = QPushButton("Сохранить")
        save_data_button.setFixedSize(250, 40)
        save_data_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                       "font-size: 16px; color: #FFFFFF")
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(save_data_button)
        buttons_layout.setContentsMargins(0, 35, 0, 0)


        dialog_layout = QVBoxLayout()
        dialog_layout.addStretch()
        dialog_layout.addWidget(title_dialog)
        dialog_layout.addLayout(name_form_layout)
        dialog_layout.addLayout(get_student_info)
        dialog_layout.addLayout(auth_form_layout)
        dialog_layout.addLayout(buttons_layout)
        dialog_layout.addStretch()
        dialog_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(dialog_layout)

