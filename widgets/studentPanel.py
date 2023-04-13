from typing import Any

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, QTableWidgetItem, QMessageBox

from service import service


class StudentPanel(QMainWindow):
    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.user_data, err = service.get_user_full_data(self.user_id, "student")
        if not err:
            self.alert_message("Произошла непредвиденная ошибка!", None)
            exit(1)

        self.rate_data, err = service.get_rating(self.user_id)
        if not err:
            self.alert_message("Произошла непредвиденная ошибка!", None)
            exit(1)


        self.setWindowTitle("Деканат.Плюс")
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setStyleSheet("background-color: #141414")

        title_widget = QLabel("Панель студента")
        title_widget.setStyleSheet("font-size: 30px; font-weight: semi-bold; color: #FFFFFF; text-align: center;")
        title_widget.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        info_student = QLabel(f"{self.user_data[2]} {self.user_data[1]} {self.user_data[3]}    {self.user_data[5]} курс    {self.user_data[6]}-{self.user_data[7]}")
        info_student.setStyleSheet("font-size: 17px; font-weight: normal; color: #FFFFFF; text-align: center;")
        info_student.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        info_widget = QVBoxLayout()
        info_widget.addWidget(title_widget)
        info_widget.addSpacing(10)
        info_widget.addWidget(info_student)
        info_widget.setAlignment(Qt.AlignmentFlag.AlignTop)


        rating_data_layout = QVBoxLayout()
        rating_data_layout.setContentsMargins(700, 20, 0, 0)
        rating_data_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        for key in self.rate_data:
            title_subject = QLabel(key)
            title_subject.setStyleSheet("font-size: 17px; font-style: italic; font-weight: bold; color: #FFFFFF; text-align: center;")
            rating_table1 = QTableWidget()
            rating_table1.setColumnCount(4)
            rating_table1.setRowCount(len(self.rate_data[key]))
            rating_table1.setHorizontalHeaderLabels(["Тема", "Оценка", "Проходной балл", "Максимальный"])
            rating_table1.verticalHeader().setVisible(False)
            rating_table1.horizontalHeader().setStyleSheet(
                "QHeaderView::section { background-color:#141414; font-size: 15px; font-weight: semi-bold; }")
            rating_table1.setStyleSheet("border: none; color: #FFFFFF;")
            rating_table1.resizeColumnsToContents()
            rating_table1.setDisabled(True)
            rating_table1.setFixedHeight(len(self.rate_data[key]) * 30 + 30)


            count = 0
            for value in self.rate_data[key]:
                rating_table1.setItem(count, 0, QTableWidgetItem(value[0]))
                if value[1] is None:
                    rating_table1.setItem(count, 1, QTableWidgetItem(""))
                else:
                    rating_table1.setItem(count, 1, QTableWidgetItem(value[1]))
                rating_table1.setItem(count, 2, QTableWidgetItem(value[2]))
                rating_table1.setItem(count, 3, QTableWidgetItem(value[3]))

                count += 1

            table_layout = QVBoxLayout()
            table_layout.addStretch()
            table_layout.addWidget(title_subject)
            table_layout.addWidget(rating_table1)
            table_layout.addStretch()

            rating_data_layout.addSpacing(40)
            rating_data_layout.addLayout(table_layout)


        data_all_users_widget = QWidget()
        data_all_users_widget.setLayout(rating_data_layout)
        data_all_users_widget.setContentsMargins(0, 0, 0, 80)

        self.scroll_widget_area = QScrollArea()
        self.scroll_widget_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_widget_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_widget_area.setWidgetResizable(True)
        self.scroll_widget_area.verticalScrollBar().setStyleSheet("QScrollBar { width: 0px; }")
        self.scroll_widget_area.setStyleSheet("QScrollArea { border: 0px solid; }")
        self.scroll_widget_area.setWidget(data_all_users_widget)


        widget_layout = QVBoxLayout()
        widget_layout.addLayout(info_widget)
        widget_layout.addWidget(self.scroll_widget_area)
        widget_layout.setContentsMargins(0, 80, 0, 0)
        widget_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(widget_layout)

        self.setCentralWidget(container)
        self.showMaximized()

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