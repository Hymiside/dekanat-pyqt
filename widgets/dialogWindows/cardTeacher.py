from typing import Any

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QDialog, QDateEdit, QPushButton, \
    QMessageBox

from service import service


class CardTeacher(QDialog):
    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.user_data, err = service.get_user_full_data(self.user_id, "teacher")
        if not err:
            self.alert_message("Произошла непредвиденная ошибка!", None)
            exit(1)

        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setWindowTitle("Деканат.Плюс")
        self.setStyleSheet("background-color: #141414")
        self.setFixedSize(850, 600)

        left_column = QVBoxLayout()
        right_column = QVBoxLayout()
        get_teacher_info = QHBoxLayout()
        get_teacher_info.setContentsMargins(0, 50, 0, 0)

        title_dialog = QLabel("Информация о преподавателе")
        title_dialog.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF;")
        title_dialog.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.last_n = QLineEdit()
        self.last_n.setPlaceholderText("Фамилия")
        self.last_n.setFixedSize(250, 45)
        self.last_n.setClearButtonEnabled(True)
        self.last_n.setText(self.user_data[2])
        self.last_n.setDisabled(True)
        self.last_n.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                  "padding: 0 0 0 10px; margin-right: 5px;")
        self.first_n = QLineEdit()
        self.first_n.setPlaceholderText("Имя")
        self.first_n.setFixedSize(250, 45)
        self.first_n.setClearButtonEnabled(True)
        self.first_n.setText(self.user_data[1])
        self.first_n.setDisabled(True)
        self.first_n.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                   "padding: 0 0 0 10px; margin-right: 5px;")
        self.middle_n = QLineEdit()
        self.middle_n.setPlaceholderText("Отчество")
        self.middle_n.setFixedSize(250, 45)
        self.middle_n.setClearButtonEnabled(True)
        self.middle_n.setText(self.user_data[3])
        self.middle_n.setDisabled(True)
        self.middle_n.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                    "padding: 0 0 0 10px;")
        name_form_layout = QHBoxLayout()
        name_form_layout.addStretch()
        name_form_layout.addWidget(self.last_n)
        name_form_layout.addWidget(self.first_n)
        name_form_layout.addWidget(self.middle_n)
        name_form_layout.addStretch()
        name_form_layout.setContentsMargins(0, 50, 0, 0)


        title_department = QLabel("Кафедра:")
        title_department.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.choice_department = QComboBox()
        self.choice_department.addItems(["МОВС", "ПМИ", "ФМ"])
        self.choice_department.setFixedSize(200, 30)
        self.choice_department.setCurrentText(self.user_data[4])
        self.choice_department.setDisabled(True)
        self.choice_department.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                             "font-size: 14px; padding: 0 0 0 10px;")
        department_layout = QHBoxLayout()
        department_layout.addWidget(title_department)
        department_layout.addWidget(self.choice_department)


        title_subject = QLabel("Предмет:")
        title_subject.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.choice_subject = QComboBox()
        self.choice_subject.addItems(["Аналитическая геометрия", "Математический анализ", "АиП", "Дискретная математика", "Базы данных и СУБД"])
        self.choice_subject.setFixedSize(200, 30)
        self.choice_subject.setCurrentText(self.user_data[5])
        self.choice_subject.setDisabled(True)
        self.choice_subject.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                          "font-size: 14px; padding: 0 0 0 10px;")
        number_course_layout = QHBoxLayout()
        number_course_layout.addWidget(title_subject)
        number_course_layout.addWidget(self.choice_subject)

        left_column.addLayout(department_layout)
        left_column.addSpacing(10)
        right_column.addLayout(number_course_layout)
        right_column.addSpacing(10)

        get_teacher_info.addStretch()
        get_teacher_info.addLayout(left_column)
        get_teacher_info.addSpacing(160)
        get_teacher_info.addLayout(right_column)
        get_teacher_info.addStretch()


        title_birthday = QLabel("Дата рождения:")
        title_birthday.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.birthday = QDateEdit(calendarPopup=True)
        self.birthday.setFixedSize(200, 30)
        date_data = self.user_data[6].split(".")
        self.birthday.setDate(QDate(int(date_data[2]), int(date_data[1]), int(date_data[0])))
        self.birthday.setDisabled(True)
        self.birthday.setStyleSheet("background-color: #424242; color: #A2A2A2; border-radius: 5px;"
                                    "font-size: 14px; padding: 0 0 0 10px; font-weight: medium;")
        birthday_layout = QHBoxLayout()
        birthday_layout.addWidget(title_birthday)
        birthday_layout.addWidget(self.birthday)


        title_email = QLabel("Email:")
        title_email.setStyleSheet("font-size: 15px; color: #FFFFFF;")
        self.email = QLineEdit()
        self.email.setFixedSize(200, 35)
        self.email.setText(self.user_data[7])
        self.email.setDisabled(True)
        self.email.setPlaceholderText("example@info.com")
        self.email.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; font-size: 14px; "
                                 "padding: 0 0 0 10px; margin-right: 5px;")
        email_layout = QHBoxLayout()
        email_layout.addWidget(title_email)
        email_layout.addWidget(self.email)

        left_column.addLayout(birthday_layout)
        left_column.addSpacing(10)
        right_column.addLayout(email_layout)
        right_column.addSpacing(10)

        get_teacher_info.addLayout(left_column)
        get_teacher_info.addLayout(right_column)


        login_teacher_title = QLabel("Логин")
        login_teacher_title.setStyleSheet("font-size: 13px; color: #FFFFFF;")
        self.login_teacher = QLineEdit()
        self.login_teacher.setPlaceholderText("Логин")
        self.login_teacher.setFixedSize(375, 45)
        self.login_teacher.setText(self.user_data[8])
        self.login_teacher.setDisabled(True)
        self.login_teacher.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                         "font-size: 14px; padding: 0 0 0 10px; margin-right: 5px;")

        login_input_layout = QVBoxLayout()
        login_input_layout.addStretch()
        login_input_layout.addWidget(login_teacher_title, alignment=Qt.AlignmentFlag.AlignLeft)
        login_input_layout.addWidget(self.login_teacher)
        login_input_layout.addStretch()


        password_teacher_title = QLabel("Пароль")
        password_teacher_title.setStyleSheet("font-size: 13px; color: #FFFFFF;")
        self.password_teacher = QLineEdit()
        self.password_teacher.setFixedSize(375, 45)
        self.password_teacher.setText(self.user_data[9])
        self.password_teacher.setDisabled(True)
        self.password_teacher.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                            "font-size: 14px; padding: 0 0 0 10px; margin-right: 5px;")
        password_input_layout = QVBoxLayout()
        password_input_layout.addStretch()
        password_input_layout.addWidget(password_teacher_title, alignment=Qt.AlignmentFlag.AlignLeft)
        password_input_layout.addWidget(self.password_teacher)
        password_input_layout.addStretch()

        auth_form_layout = QHBoxLayout()
        auth_form_layout.addStretch()
        auth_form_layout.addLayout(login_input_layout)
        auth_form_layout.addLayout(password_input_layout)
        auth_form_layout.addStretch()
        auth_form_layout.setContentsMargins(0, 25, 0, 0)


        self.edit_data_button = QPushButton("Редактировать")
        self.edit_data_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_data_button.setFixedSize(250, 40)
        self.edit_data_button.clicked.connect(self.edit_data)
        self.edit_data_button.setCheckable(True)
        self.edit_data_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                            "font-size: 16px; color: #FFFFFF")
        save_changes_button = QPushButton("Сохранить изменения")
        save_changes_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        save_changes_button.setFixedSize(250, 40)
        save_changes_button.clicked.connect(self.save_changes)
        save_changes_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; font-size: 16px;"
                                          " color: #FFFFFF")
        delete_button = QPushButton("Удалить")
        delete_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        delete_button.setFixedSize(250, 40)
        delete_button.clicked.connect(self.delete_user)
        delete_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; font-size: 16px;"
                                    " color: #FFFFFF")
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.edit_data_button)
        buttons_layout.addWidget(save_changes_button)
        buttons_layout.addWidget(delete_button)
        buttons_layout.addStretch()
        buttons_layout.setContentsMargins(0, 35, 0, 0)


        dialog_layout = QVBoxLayout()
        dialog_layout.addStretch()
        dialog_layout.addWidget(title_dialog)
        dialog_layout.addLayout(name_form_layout)
        dialog_layout.addLayout(get_teacher_info)
        dialog_layout.addLayout(auth_form_layout)
        dialog_layout.addLayout(buttons_layout)
        dialog_layout.addStretch()
        dialog_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(dialog_layout)

    def edit_data(self, checked: bool):
        if checked:
            self.edit_data_button.setCheckable(False)
            self.edit_data_button.setText("Остановить редактирование")

            self.last_n.setDisabled(False)
            self.first_n.setDisabled(False)
            self.middle_n.setDisabled(False)
            self.choice_subject.setDisabled(False)
            self.choice_department.setDisabled(False)
            self.birthday.setDisabled(False)
            self.email.setDisabled(False)

        else:
            self.edit_data_button.setCheckable(True)
            self.edit_data_button.setText("Редактировать")

            self.last_n.setDisabled(True)
            self.first_n.setDisabled(True)
            self.middle_n.setDisabled(True)
            self.choice_subject.setDisabled(True)
            self.choice_department.setDisabled(True)
            self.birthday.setDisabled(True)
            self.email.setDisabled(True)

    def save_changes(self) -> None:
        user_data = [
            self.last_n.text().strip(), self.first_n.text().strip(), self.middle_n.text().strip(),
            self.choice_department.currentText(), self.choice_subject.currentText(),
            self.birthday.text(), self.email.text(), self.user_id
        ]

        if not self.first_n.text().strip() or not self.last_n.text().strip() or not self.middle_n.text().strip() or not self.email.text():
            self.alert_message("Заполните все поля!", None)
            return

        res = service.update_user(user_data, "teacher")
        if not res:
            self.alert_message("Произошла ошибка, попробуйте еще раз!", None)
            return
        self.close()

    def delete_user(self):
        res = service.delete_user(self.user_id, "teacher")
        if not res:
            self.alert_message("Произошла ошибка, попробуйте еще раз!", None)
            return

        self.close()

    @staticmethod
    def alert_message(info: str, more_info: Any) -> None:
        alert = QMessageBox()
        alert.setText(info)
        if more_info is not None:
            alert.setDetailedText(more_info)
        alert.setWindowIcon(QtGui.QIcon("assets/error.ico"))
        alert.setWindowTitle("Что-то пошло не так")
        alert.setStandardButtons(QMessageBox.StandardButton.Close)
        alert.setStyleSheet("color: #141414; font-size: 14px; font-weight: semi-bold;")
        alert.exec()