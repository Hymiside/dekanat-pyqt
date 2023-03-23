from PyQt6.QtWidgets import QApplication
from widgets import auth


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet("""
        QRadioButton {
            margin: 0 0 0 25px;
            font-size: 15px;
            color: #646464;            
        }
        
        QRadioButton:checked {
            color: #fff;
        }
    """)

    auth_window = auth.Auth()
    app.exec()
