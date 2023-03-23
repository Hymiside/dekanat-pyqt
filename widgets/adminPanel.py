from typing import List

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, \
    QRadioButton, QScrollArea

from service import service
from widgets.dialogWindows import createStudent, cardStudent


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

        add_button_student = QPushButton("Добавить студента")
        add_button_student.setFixedSize(225, 40)
        add_button_student.clicked.connect(self.create_student)
        add_button_student.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                         "font-size: 16px; color: #FFFFFF")

        download_button_student = QPushButton("Скачать данные студентов")
        download_button_student.setFixedSize(240, 40)
        download_button_student.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                              "font-size: 16px; color: #FFFFFF")

        add_button_teacher = QPushButton("Добавить преподавателя")
        add_button_teacher.setFixedSize(225, 40)
        add_button_teacher.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                         "font-size: 16px; color: #FFFFFF")

        add_buttons_layout = QHBoxLayout()
        add_buttons_layout.addStretch()
        add_buttons_layout.addWidget(add_button_student)
        add_buttons_layout.addWidget(download_button_student)
        add_buttons_layout.addWidget(add_button_teacher)
        add_buttons_layout.setContentsMargins(0, 35, 0, 0)
        add_buttons_layout.addStretch()


        search_line_user = QLineEdit()
        search_line_user.setFixedSize(700, 60)
        search_line_user.setContentsMargins(0, 20, 0, 0)
        search_line_user.setClearButtonEnabled(True)
        search_line_user.setPlaceholderText("Введите фамилию")
        search_line_user.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                       "font-size: 14px; padding: 0 0 0 10px;")


        self.radio_button_student = QRadioButton("Студенты")
        self.radio_button_student.setChecked(True)
        self.radio_button_student.toggled.connect(lambda: self.change_view(self.radio_button_student))
        self.radio_button_teacher = QRadioButton("Преподаватели")
        self.radio_button_teacher.toggled.connect(lambda: self.change_view(self.radio_button_teacher))


        radio_buttons_layout = QHBoxLayout()
        radio_buttons_layout.addStretch()
        radio_buttons_layout.addWidget(self.radio_button_student)
        radio_buttons_layout.addWidget(self.radio_button_teacher)
        radio_buttons_layout.addStretch()
        radio_buttons_layout.setContentsMargins(0, 10, 0, 0)


        users_data = service.get_all_users_students()
        # users_data = []
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
                    button_more_user = QPushButton("Подробнее")
                    button_more_user.clicked.connect(lambda checked, user_id=i[0]: self.open_card(user_id))
                    button_more_user.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                                   "font-size: 13px; color: #FFFFFF; width: 120px; height: 30px; margin-left: 205px;")
                    fullname_text = QLabel(f"{i[1]} {i[2]} {i[3]}")
                    fullname_text.setStyleSheet("font-size: 15px; color: #FFFFFF;")

                    role_text = QLabel(f"{i[4]}-{i[5]}")
                    role_text.setStyleSheet("font-size: 14px; color: #FFFFFF; margin-left: 80px; font-style: italic;")

                    column_buttons_more.addWidget(button_more_user)
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
        widget_layout.addWidget(search_line_user, alignment=Qt.AlignmentFlag.AlignHCenter)
        widget_layout.addLayout(radio_buttons_layout)
        widget_layout.addWidget(self.scroll_widget_area)
        widget_layout.setContentsMargins(0, 80, 0, 0)
        widget_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(widget_layout)

        self.setCentralWidget(container)
        self.showMaximized()

    @staticmethod
    def open_card(user_id: int):
        create_student_dialog_window = cardStudent.CardStudent(user_id)
        create_student_dialog_window.exec()

    @staticmethod
    def create_student():
        create_student_dialog_window = createStudent.CreateStudent()
        create_student_dialog_window.exec()

    def change_view(self, b):
        if b.text() == "Студенты" and b.isChecked():
            response = service.get_all_users_students()
            users_data_widget = self.fill_widget_data(response)
            self.scroll_widget_area.setWidget(users_data_widget)


        if b.text() == "Преподаватели" and b.isChecked():
            response = service.get_all_users_teachers()
            users_data_widget = self.fill_widget_data(response)
            self.scroll_widget_area.setWidget(users_data_widget)


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
                    button_more_user = QPushButton("Подробнее")
                    button_more_user.clicked.connect(lambda checked, user_id=i[0]: self.open_card(user_id))
                    button_more_user.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                                   "font-size: 13px; color: #FFFFFF; width: 120px; height: 30px; margin-left: 205px;")
                    fullname_text = QLabel(f"{i[1]} {i[2]} {i[3]}")
                    fullname_text.setStyleSheet("font-size: 15px; color: #FFFFFF;")

                    role_text = QLabel(f"{i[4]}-{i[5]}")
                    role_text.setStyleSheet("font-size: 14px; color: #FFFFFF; margin-left: 80px; font-style: italic;")

                    column_buttons_more.addWidget(button_more_user)
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
