from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QTextBrowser


class SessionWidget(QWidget):
    session_state = Signal(str)

    def __init__(self, parent):
        super(SessionWidget, self).__init__(parent)

        self.__user_name_line_edit = QLineEdit()
        self.__password_line_edit = QLineEdit()
        self.__token_line_edit = QLineEdit()

        # Aufgabe 1.1

        self.__login_push_button = QPushButton("Login")
        self.__logout_push_button = QPushButton("Logout")

        # Aufgabe 1.2

        # Aufgabe 1.5

        self.__log_text_browser = QTextBrowser()

        grid_layout = QGridLayout()

        grid_layout.addWidget(QLabel("Benutzername"), 1, 1)
        grid_layout.addWidget(self.__user_name_line_edit, 1, 2)

        grid_layout.addWidget(QLabel("Passwort"), 2, 1)
        grid_layout.addWidget(self.__password_line_edit, 2, 2)

        grid_layout.addWidget(QLabel("Token"), 3, 1)
        grid_layout.addWidget(self.__token_line_edit, 3, 2)

        grid_layout.addWidget(self.__login_push_button, 4, 1)
        grid_layout.addWidget(self.__logout_push_button, 4, 2)

        grid_layout.addWidget(self.__log_text_browser, 5, 1, 1, 2)

        self.setLayout(grid_layout)

        self.__usernames = list()
        self.__passwords = list()

        self.__usernames.append("user 1")
        self.__passwords.append("geheim")

        self.__usernames.append("user 2")
        self.__passwords.append("abc123")

        self.__usernames.append("admin")
        self.__passwords.append("geheim")

        self.__tokens = dict()
        self.__tokens["1234"] = "./nft_1.jpg"
        self.__tokens["AFFE"] = "./nft_2.jpg"
        self.__tokens["BE3F"] = "./nft_3.jpg"
        self.__tokens["C07A"] = "./nft_4.jpg"

    def check_login(self):
        # Aufgabe 1.3
        pass

        # Aufgabe 1.4

        # Aufgabe 1.5

        # Aufgabe 1.6

    def append_log(self, message):
        # Aufgabe 1.4
        pass

    def reset(self):
        # Aufgabe 1.5
        pass

        # Aufgabe 1.6
