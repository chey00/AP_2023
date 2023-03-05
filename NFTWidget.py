from PySide6.QtCore import Slot, QTimer, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QSlider, QPushButton, QColorDialog

from NFTLabel import NFTLabel


class NFTWidget(QWidget):
    state_handler = Slot(str)
    set_timer = Slot(int)
    set_color = Slot()

    def __init__(self, parent):
        super(NFTWidget, self).__init__(parent)

        self.__timer = QTimer()
        self.__slider = QSlider()
        self.__label = NFTLabel(parent)
        self.__push_button = QPushButton("Farbauswahl ...")

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.__label, 1, 1, 1, 3)
        grid_layout.addWidget(self.__slider, 2, 1, 1, 2)
        grid_layout.addWidget(self.__push_button, 2, 3)

        self.setLayout(grid_layout)

        self.close_vault()

        # Aufgabe 2.2

        # Aufgabe 2.4

    def state_handler(self, state: str):
        # Aufgabe 2.1
        pass

    def close_vault(self):
        # Aufgabe 2.1
        pass

        # Aufgabe 2.2

    def open_vault(self, ntf_name):
        # Aufgabe 2.1
        pass

        # Aufgabe 2.2

#    def set_timer(self, msec: int):
        # Aufgabe 2.2

    def set_color(self):
        # Aufgabe 2.4
        pass
