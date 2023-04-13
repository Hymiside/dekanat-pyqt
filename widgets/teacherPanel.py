from typing import List, Any

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QScrollArea, \
    QMessageBox

from service import service
from widgets.dialogWindows import createRateStudent


class TeacherPanel(QMainWindow):
    def __init__(self, user_id: int):
        super().__init__()

        self.user_id = user_id
        self.user_data, err = service.get_user_full_data(self.user_id, "teacher")
        if not err:
            self.alert_message("Произошла непредвиденная ошибка!", None)
            exit(1)

        self.setWindowTitle("Деканат.Плюс")
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setStyleSheet("background-color: #141414")

        title_widget = QLabel("Панель преподавателя")
        title_widget.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; "
                                   "text-align: center;")
        title_widget.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        info_teacher = QLabel(f"{self.user_data[1]} {self.user_data[2]} {self.user_data[3]}    Кафедра: {self.user_data[4]}    Предмет: {self.user_data[5]}")
        info_teacher.setStyleSheet("font-size: 17px; font-weight: normal; color: #FFFFFF; text-align: center;")
        info_teacher.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        self.search_line_user = QLineEdit()
        self.search_line_user.textChanged.connect(self.change_search_line)
        self.search_line_user.setFixedSize(700, 60)
        self.search_line_user.setContentsMargins(0, 20, 0, 0)
        self.search_line_user.setClearButtonEnabled(True)
        self.search_line_user.setPlaceholderText("Введите фамилию")
        self.search_line_user.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                            "font-size: 14px; padding: 0 0 0 10px;")

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
                    more_user_button = QPushButton("Поставить оценку")
                    more_user_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                    more_user_button.clicked.connect(lambda checked, user_id=i[0], subject=self.user_data[5]: self.card_user(user_id, subject))
                    more_user_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                                   "font-size: 13px; color: #FFFFFF; width: 130px; height: 30px; margin-left: 205px;")
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
        widget_layout.addSpacing(10)
        widget_layout.addWidget(info_teacher)
        widget_layout.addSpacing(15)
        widget_layout.addWidget(self.search_line_user, alignment=Qt.AlignmentFlag.AlignHCenter)
        widget_layout.addWidget(self.scroll_widget_area)
        widget_layout.setContentsMargins(0, 80, 0, 0)
        widget_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(widget_layout)

        self.setCentralWidget(container)
        self.showMaximized()

    def card_user(self, user_id: int, subject: str):
        card_student_dialog_window = createRateStudent.CreateRate(user_id, subject)
        card_student_dialog_window.exec()
        self.update_view()

    def update_view(self):
        response = service.get_all_users_students("preview")
        users_data_widget = self.fill_widget_data(response)
        self.scroll_widget_area.setWidget(users_data_widget)

    def change_search_line(self):
        value = f"%{self.search_line_user.text().strip().title()}%"
        response = service.get_all_users_filter_search_line(value, "student")
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
                    more_user_button = QPushButton("Поставить оценку")
                    more_user_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                    more_user_button.clicked.connect(lambda checked, user_id=i[0]: self.card_user(user_id))
                    more_user_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                                   "font-size: 13px; color: #FFFFFF; width: 130px; height: 30px; margin-left: 205px;")
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
        return data_all_users_widget

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