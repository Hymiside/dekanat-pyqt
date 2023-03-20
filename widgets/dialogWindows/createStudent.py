from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QDialog, QSpinBox, QDateEdit

from service import service


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent=parent)
        self.input_data = self.text()
        self.setPlaceholderText('2342-234234')

    def focusInEvent(self, event):
        self.setInputMask('0000-000000')

    def focusOutEvent(self, event):
        self.input_data = self.text()
        if self.input_data.strip() == "-":
            self.setInputMask('')


class CreateStudent(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("assets/main.ico"))
        self.setWindowTitle("Деканат.Плюс")
        self.setStyleSheet("background-color: #141414")
        self.setFixedSize(850, 700)

        left_column = QVBoxLayout()
        right_column = QVBoxLayout()
        get_student_info = QHBoxLayout()
        get_student_info.setContentsMargins(0, 50, 0, 0)

        title_dialog = QLabel("Создание нового студента")
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


        self.choice_form_edu = QComboBox()
        self.choice_form_edu.addItems(["Бакалавриат", "Магистратура", "Специалитет"])
        self.choice_form_edu.setFixedSize(200, 30)
        self.choice_form_edu.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                           "font-size: 14px; padding: 0 0 0 10px;")
        self.title_form_edu = QLabel("Форма обучения:")
        self.title_form_edu.setStyleSheet("font-size: 15px; color: #FFFFFF;")

        form_edu_layout = QHBoxLayout()
        form_edu_layout.addWidget(self.title_form_edu)
        form_edu_layout.addWidget(self.choice_form_edu)


        self.number_course = QSpinBox()
        self.number_course.setMaximum(5)
        self.number_course.setMinimum(1)
        self.number_course.setFixedSize(100, 30)
        self.number_course.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                         "font-size: 14px; padding: 0 0 0 10px;")
        self.title_number_course = QLabel("Курс обучения:")
        self.title_number_course.setStyleSheet("font-size: 15px; color: #FFFFFF;")

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

        self.choice_group_name = QComboBox()
        self.choice_group_name.addItems(["ПМИ", "ФИТ", "ИТХ", "ИТС", "КМБ", "МММ"])
        self.choice_group_name.setFixedSize(200, 30)
        self.choice_group_name.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                             "font-size: 14px; padding: 0 0 0 10px;")
        self.title_group_name = QLabel("Направление:")
        self.title_group_name.setStyleSheet("font-size: 15px; color: #FFFFFF;")

        group_name_layout = QHBoxLayout()
        group_name_layout.addWidget(self.title_group_name)
        group_name_layout.addWidget(self.choice_group_name)


        self.number_group = QSpinBox()
        self.number_group.setMaximum(10)
        self.number_group.setMinimum(1)
        self.number_group.setFixedSize(100, 30)
        self.number_group.setStyleSheet("background-color: #424242; color: #FFFFFF; border-radius: 5px;"
                                        "font-size: 14px; padding: 0 0 0 10px;")
        self.title_number_group = QLabel("Номер группы:")
        self.title_number_group.setStyleSheet("font-size: 15px; color: #FFFFFF;")

        number_group_layout = QHBoxLayout()
        number_group_layout.addWidget(self.title_number_group)
        number_group_layout.addWidget(self.number_group)


        left_column.addLayout(group_name_layout)
        left_column.addSpacing(10)
        right_column.addLayout(number_group_layout)
        right_column.addSpacing(10)

        get_student_info.addLayout(left_column)
        get_student_info.addLayout(right_column)


        self.birthday = QDateEdit(calendarPopup=True)
        self.birthday.setFixedSize(200, 30)
        self.birthday.setStyleSheet("background-color: #424242; color: #A2A2A2; border-radius: 5px;"
                                    "font-size: 14px; padding: 0 0 0 10px; font-weight: medium;")
        title_birthday = QLabel("Дата рождения:")
        title_birthday.setStyleSheet("font-size: 15px; color: #FFFFFF;")

        birthday_layout = QHBoxLayout()
        birthday_layout.addWidget(title_birthday)
        birthday_layout.addWidget(self.birthday)

        self.passport_id = LineEdit()
        self.passport_id.setFixedSize(130, 30)
        self.passport_id.setStyleSheet("color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 5px; "
                                       "font-size: 14px; padding: 0 0 0 10px; margin-right: 5px;")
        title_passport_id = QLabel("Данные паспорта:")
        title_passport_id.setStyleSheet("font-size: 15px; color: #FFFFFF;")

        passport_id_layout = QHBoxLayout()
        passport_id_layout.addWidget(title_passport_id)
        passport_id_layout.addWidget(self.passport_id)


        left_column.addLayout(birthday_layout)
        left_column.addSpacing(10)
        right_column.addLayout(passport_id_layout)
        right_column.addSpacing(10)

        get_student_info.addLayout(left_column)
        get_student_info.addLayout(right_column)


        dialog_layout = QVBoxLayout()
        dialog_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        dialog_layout.setContentsMargins(0, 50, 0, 0)
        dialog_layout.addWidget(title_dialog)
        dialog_layout.addLayout(name_form_layout)
        dialog_layout.addLayout(get_student_info)

        self.setLayout(dialog_layout)


