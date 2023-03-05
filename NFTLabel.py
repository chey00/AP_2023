from PySide6.QtGui import QPaintEvent, QPainter, QColor, QPixmap, QBrush
from PySide6.QtWidgets import QLabel


class NFTLabel(QLabel):
    def __init__(self, parent):
        super(NFTLabel, self).__init__(parent)

        self.__toggle = False
        self.__color = QColor("red")
        self.__pixmap = None

    def paintEvent(self, arg__1: QPaintEvent) -> None:
        super(NFTLabel, self).paintEvent(arg__1)

        if self.__pixmap:
            if self.__toggle:
                # Aufgabe 2.3

                self.__toggle = False
            else:
                self.__toggle = True

    def set_color(self, color):
        # Aufgabe 2.4
        pass

    def set_nft(self, ntf_name):
        # Aufgabe 2.1
        pass
