from typing import List

import pandas as pd
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, \
    QRadioButton, QScrollArea, QFileDialog

from service import service
from widgets.dialogWindows import createStudent, cardStudent, createTeacher, cardTeacher


class AdminPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Деканат.Плюс")
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setStyleSheet("background-color: #141414")


        title_widget = QLabel("Панель администратора")
        title_widget.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; "
                                   "text-align: center;")
        title_widget.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        add_student_button = QPushButton("Добавить студента")
        add_student_button.setFixedSize(225, 40)
        add_student_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        add_student_button.clicked.connect(self.create_student)
        add_student_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                         "font-size: 16px; color: #FFFFFF")

        download_button_student = QPushButton("Скачать данные студентов")
        download_button_student.setFixedSize(240, 40)
        download_button_student.clicked.connect(self.download_all_students)
        download_button_student.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        download_button_student.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                              "font-size: 16px; color: #FFFFFF")

        add_teacher_button = QPushButton("Добавить преподавателя")
        add_teacher_button.setFixedSize(225, 40)
        add_teacher_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        add_teacher_button.clicked.connect(self.create_teacher)
        add_teacher_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                         "font-size: 16px; color: #FFFFFF")

        add_buttons_layout = QHBoxLayout()
        add_buttons_layout.addStretch()
        add_buttons_layout.addWidget(add_student_button)
        add_buttons_layout.addWidget(download_button_student)
        add_buttons_layout.addWidget(add_teacher_button)
        add_buttons_layout.setContentsMargins(0, 35, 0, 0)
        add_buttons_layout.addStretch()


        self.search_line_user = QLineEdit()
        self.search_line_user.textChanged.connect(self.change_search_line)
        self.search_line_user.setFixedSize(700, 60)
        self.search_line_user.setContentsMargins(0, 20, 0, 0)
        self.search_line_user.setClearButtonEnabled(True)
        self.search_line_user.setPlaceholderText("Введите фамилию")
        self.search_line_user.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                            "font-size: 14px; padding: 0 0 0 10px;")


        self.radio_button_student = QRadioButton("Студенты")
        self.radio_button_student.setChecked(True)
        self.radio_button_student.toggled.connect(self.update_view)
        self.radio_button_student.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radio_button_teacher = QRadioButton("Преподаватели")
        self.radio_button_teacher.toggled.connect(self.update_view)
        self.radio_button_teacher.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))



        radio_buttons_layout = QHBoxLayout()
        radio_buttons_layout.addStretch()
        radio_buttons_layout.addWidget(self.radio_button_student)
        radio_buttons_layout.addWidget(self.radio_button_teacher)
        radio_buttons_layout.addStretch()
        radio_buttons_layout.setContentsMargins(0, 10, 0, 0)


        users_data = service.get_all_users_students("preview")
        data_all_users_layout = QVBoxLayout()
        data_all_users_layout.setContentsMargins(0, 60, 0, 80)

        column_buttons_more = QVBoxLayout()
        column_text_fullname = QVBoxLayout()
        column_text_role = QVBoxLayout()

        match not users_data:
            case True:
                no_users_text = QLabel("В системе пока нет пользователей.\nДобавьте их через кнопки выше и они сразу отобразятся на главном экране.")
                no_users_text.setStyleSheet("font-size: 16px; color: #FFFFFF; font-style: italic;")
                no_users_text.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                data_all_users_layout.addWidget(no_users_text)

            case False:
                for i in users_data:
                    more_user_button = QPushButton("Подробнее")
                    more_user_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                    more_user_button.clicked.connect(lambda checked, user_id=i[0]: self.card_user(user_id))
                    more_user_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                                   "font-size: 13px; color: #FFFFFF; width: 120px; height: 30px; margin-left: 205px;")
                    fullname_text = QLabel(f"{i[1]} {i[2]} {i[3]}")
                    fullname_text.setStyleSheet("font-size: 15px; color: #FFFFFF;")

                    role_text = QLabel(f"{i[4]}-{i[5]}")
                    role_text.setStyleSheet("font-size: 14px; color: #FFFFFF; margin-left: 80px; font-style: italic;")

                    column_buttons_more.addWidget(more_user_button)
                    column_text_fullname.addWidget(fullname_text)
                    column_text_role.addWidget(role_text)

                    user_data_layout = QHBoxLayout()
                    user_data_layout.addStretch()
                    user_data_layout.addLayout(column_text_fullname)
                    user_data_layout.addLayout(column_text_role)
                    user_data_layout.addLayout(column_buttons_more)
                    user_data_layout.addStretch()
                    user_data_layout.setSpacing(15)

                    data_all_users_layout.addLayout(user_data_layout)
                    data_all_users_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        data_all_users_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        data_all_users_widget = QWidget()
        data_all_users_widget.setLayout(data_all_users_layout)

        self.scroll_widget_area = QScrollArea()
        self.scroll_widget_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_widget_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_widget_area.setWidgetResizable(True)
        self.scroll_widget_area.verticalScrollBar().setStyleSheet("QScrollBar { width: 0px; }")
        self.scroll_widget_area.setStyleSheet("QScrollArea { border: 0px solid; }")
        self.scroll_widget_area.setWidget(data_all_users_widget)


        widget_layout = QVBoxLayout()
        widget_layout.addWidget(title_widget)
        widget_layout.addLayout(add_buttons_layout)
        widget_layout.addWidget(self.search_line_user, alignment=Qt.AlignmentFlag.AlignHCenter)
        widget_layout.addLayout(radio_buttons_layout)
        widget_layout.addWidget(self.scroll_widget_area)
        widget_layout.setContentsMargins(0, 80, 0, 0)
        widget_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(widget_layout)

        self.setCentralWidget(container)
        self.showMaximized()

    def card_user(self, user_id: int):
        if self.radio_button_student.isChecked():
            card_student_dialog_window = cardStudent.CardStudent(user_id)
            card_student_dialog_window.exec()
            self.update_view()

        elif self.radio_button_teacher.isChecked():
            card_teacher_dialog_window = cardTeacher.CardTeacher(user_id)
            card_teacher_dialog_window.exec()
            self.update_view()

    def create_student(self):
        create_student_dialog_window = createStudent.CreateStudent()
        create_student_dialog_window.exec()
        self.update_view()

    def create_teacher(self):
        create_teacher_dialog_window = createTeacher.CreateTeacher()
        create_teacher_dialog_window.exec()
        self.update_view()

    def update_view(self):
        if self.radio_button_student.isChecked():
            response = service.get_all_users_students("preview")
            users_data_widget = self.fill_widget_data(response)
            self.scroll_widget_area.setWidget(users_data_widget)

        elif self.radio_button_teacher.isChecked():
            response = service.get_all_users_teacher("preview")
            users_data_widget = self.fill_widget_data(response)
            self.scroll_widget_area.setWidget(users_data_widget)

    def change_search_line(self):
        value = f"%{self.search_line_user.text().strip().title()}%"

        if self.radio_button_student.isChecked():
            response = service.get_all_users_filter_search_line(value, "student")
            users_data_widget = self.fill_widget_data(response)
            self.scroll_widget_area.setWidget(users_data_widget)

        elif self.radio_button_teacher.isChecked():
            response = service.get_all_users_filter_search_line(value, "teacher")
            users_data_widget = self.fill_widget_data(response)
            self.scroll_widget_area.setWidget(users_data_widget)

    def download_all_students(self):
        users_data = service.get_all_users_students("full")
        data_for_file = {
            'Фамилия': [],
            'Имя': [],
            'Отчество': [],
            'Форма обучения': [],
            'Курс обучения': [],
            'Направление': [],
            'Номер группы': [],
            'Дата рождения': [],
            'Данные паспорта': [],
            'Логин': [],
            'Пароль': []
        }

        for value in users_data:
            data_for_file['Фамилия'].append(value[0])
            data_for_file['Имя'].append(value[1])
            data_for_file['Отчество'].append(value[2])
            data_for_file['Форма обучения'].append(value[3])
            data_for_file['Курс обучения'].append(value[4])
            data_for_file['Направление'].append(value[5])
            data_for_file['Номер группы'].append(value[6])
            data_for_file['Дата рождения'].append(value[7])
            data_for_file['Данные паспорта'].append(value[8])
            data_for_file['Логин'].append(value[9])
            data_for_file['Пароль'].append(value[10])

        try:
            file_path = QFileDialog.getSaveFileName(self, "Сохранить файл", "all-students.xlsx",
                                                    "Excel Files (*.xls *.xlsx)")
            writer = pd.ExcelWriter(file_path[0], engine='xlsxwriter')
            df = pd.DataFrame(data_for_file)
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.close()

        except Exception as err:
            print(err)

    def fill_widget_data(self, users_data: List) -> QWidget:
        data_all_users_layout = QVBoxLayout()
        data_all_users_layout.setContentsMargins(0, 60, 0, 80)

        column_buttons_more = QVBoxLayout()
        column_text_fullname = QVBoxLayout()
        column_text_role = QVBoxLayout()

        match not users_data:
            case True:
                no_users_text = QLabel(
                    "В системе пока нет пользователей.\nДобавьте их через кнопки выше и они сразу отобразятся на главном экране.")
                no_users_text.setStyleSheet("font-size: 16px; color: #FFFFFF; font-style: italic;")
                no_users_text.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                data_all_users_layout.addWidget(no_users_text)

            case False:
                for i in users_data:
                    more_user_button = QPushButton("Подробнее")
                    more_user_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                    more_user_button.clicked.connect(lambda checked, user_id=i[0]: self.card_user(user_id))
                    more_user_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                                   "font-size: 13px; color: #FFFFFF; width: 120px; height: 30px; margin-left: 205px;")
                    fullname_text = QLabel(f"{i[1]} {i[2]} {i[3]}")
                    fullname_text.setStyleSheet("font-size: 15px; color: #FFFFFF;")

                    if self.radio_button_student.isChecked():
                        role_text = QLabel(f"{i[4]}-{i[5]}")
                    elif self.radio_button_teacher.isChecked():
                        role_text = QLabel(i[4])

                    role_text.setStyleSheet("font-size: 14px; color: #FFFFFF; margin-left: 80px; font-style: italic;")
                    column_buttons_more.addWidget(more_user_button)
                    column_text_fullname.addWidget(fullname_text)
                    column_text_role.addWidget(role_text)

                    user_data_layout = QHBoxLayout()
                    user_data_layout.addStretch()
                    user_data_layout.addLayout(column_text_fullname)
                    user_data_layout.addLayout(column_text_role)
                    user_data_layout.addLayout(column_buttons_more)
                    user_data_layout.addStretch()
                    user_data_layout.setSpacing(15)

                    data_all_users_layout.addLayout(user_data_layout)
                    data_all_users_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        data_all_users_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        data_all_users_widget = QWidget()
        data_all_users_widget.setLayout(data_all_users_layout)
        return data_all_users_widget
