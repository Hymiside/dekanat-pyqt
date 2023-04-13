from typing import Any

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QComboBox, QDialog, QSpinBox, QPushButton, QMessageBox

from service import service


class CreateRate(QDialog):
    def __init__(self, user_id: int, subject: str):
        super().__init__()

        self.user_id = user_id
        user_data, err = service.get_user_full_data(self.user_id, "student")
        if not err:
            self.alert_message("Произошла непредвиденная ошибка!", None)
            exit(1)

        self.subject = subject
        match self.subject:
            case "Аналитическая геометрия":
                topic = ["КТ1", "КТ2", "КТ3", "КТ4", "КТ5"]
            case "Математический анализ":
                topic = ["КТ1", "КТ2", "КТ3", "КТ4", "КТ5"]
            case "АиП":
                topic = ["КТ1", "КТ2", "КТ3"]
            case "Дискретная математика":
                topic = ["КТ1", "КТ2", "КТ3", "КТ4"]


        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setWindowTitle("Деканат.Плюс")
        self.setStyleSheet("background-color: #141414")
        self.setFixedSize(400, 600)

        title_dialog = QLabel("Поставить оценку")
        title_dialog.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF;")
        title_dialog.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        full_name_label = QLabel("ФИО")
        full_name_label.setStyleSheet("font-size: 18px; font-weight: bold; font-style: italic; color: #FFFFFF;")
        full_name = QLabel(f"{user_data[2]} {user_data[1]} {user_data[3]}")
        full_name.setStyleSheet("font-size: 17px; color: #FFFFFF;")

        direction_education_label = QLabel("Форма обучения")
        direction_education_label.setStyleSheet("font-size: 18px; font-weight: bold; font-style: italic; color: #FFFFFF;")
        direction_education = QLabel(f"{user_data[4]}")
        direction_education.setStyleSheet("font-size: 17px; color: #FFFFFF;")
        info_education = QLabel(f"{user_data[5]} курс   {user_data[6]}-{user_data[7]}")
        info_education.setStyleSheet("font-size: 17px; color: #FFFFFF;")

        fullname_layout = QVBoxLayout()
        fullname_layout.addSpacing(20)
        fullname_layout.addWidget(full_name_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        fullname_layout.addWidget(full_name, alignment=Qt.AlignmentFlag.AlignHCenter)
        fullname_layout.addSpacing(20)
        fullname_layout.addWidget(direction_education_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        fullname_layout.addWidget(direction_education, alignment=Qt.AlignmentFlag.AlignHCenter)
        fullname_layout.addWidget(info_education, alignment=Qt.AlignmentFlag.AlignHCenter)
        fullname_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        title_choice_topic = QLabel("Выберите КТ:")
        title_choice_topic.setStyleSheet("font-size: 15px; color: #FFFFFF; font-style: italic;")
        self.choice_topic = QComboBox()
        self.choice_topic.addItems(topic)
        self.choice_topic.setFixedSize(170, 30)
        self.choice_topic.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                        "font-size: 14px; padding: 0 0 0 10px;")
        choice_topic_layout = QVBoxLayout()
        choice_topic_layout.addWidget(title_choice_topic)
        choice_topic_layout.addWidget(self.choice_topic)


        title_choice_rate = QLabel("Поставьте оценку:")
        title_choice_rate.setStyleSheet("font-size: 15px; color: #FFFFFF; font-style: italic;")
        self.choice_rate = QSpinBox()
        self.choice_rate.setMaximum(30)
        self.choice_rate.setMinimum(1)
        self.choice_rate.setFixedSize(170, 30)
        self.choice_rate.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                       "font-size: 14px; padding: 0 0 0 10px;")
        choice_rate_layout = QVBoxLayout()
        choice_rate_layout.addWidget(title_choice_rate)
        choice_rate_layout.addWidget(self.choice_rate)

        rate_input_layout = QVBoxLayout()
        rate_input_layout.addStretch()
        rate_input_layout.addLayout(choice_topic_layout)
        rate_input_layout.addSpacing(10)
        rate_input_layout.addLayout(choice_rate_layout)
        rate_input_layout.addStretch()
        rate_input_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        save_data_button = QPushButton("Сохранить")
        save_data_button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        save_data_button.setFixedSize(250, 40)
        save_data_button.clicked.connect(self.save_data)
        save_data_button.setStyleSheet("background-color: #424242; border: none; border-radius: 5px; "
                                       "font-size: 16px; color: #FFFFFF")


        dialog_layout = QVBoxLayout()
        dialog_layout.addStretch()
        dialog_layout.addWidget(title_dialog, alignment=Qt.AlignmentFlag.AlignHCenter)
        dialog_layout.addLayout(fullname_layout)
        dialog_layout.addSpacing(30)
        dialog_layout.addLayout(rate_input_layout)
        dialog_layout.addSpacing(40)
        dialog_layout.addWidget(save_data_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        dialog_layout.addStretch()
        dialog_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(dialog_layout)

    def save_data(self) -> None:
        rate_data = [self.choice_rate.text(), self.user_id, self.choice_topic.currentText(), self.subject]

        res = service.update_rate(rate_data)
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