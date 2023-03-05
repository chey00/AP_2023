from PySide6.QtWidgets import QTabWidget

from ChartWidget import ChartWidget
from NFTWidget import NFTWidget
from SessionWidget import SessionWidget


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        session_tab = SessionWidget(parent)
        nft_tab = NFTWidget(parent)
        chart_tab = ChartWidget(parent)

        self.addTab(session_tab, "Session")
        self.addTab(nft_tab, "Non-Fungible Token")
        self.addTab(chart_tab, "Charts")

        # Aufgabe 1.6

        # Aufgabe 2
        # nft_tab.state_handler("nft_1.jpg")
        # self.setCurrentWidget(nft_tab)

        # Aufgabe 3
        # self.setCurrentWidget(chart_tab)

