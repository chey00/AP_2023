from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt


class ChartWidget(QChartView):
    def __init__(self, parent):
        super(ChartWidget, self).__init__(parent)

        series_1 = QLineSeries()
        series_1.setName("NFT 1")
        series_1.append(1*60*60*1000, 4.23)
        series_1.append(2*60*60*1000, 3.67)
        series_1.append(3*60*60*1000, 9.12)
        series_1.append(4*60*60*1000, 7.69)

        series_2 = QLineSeries()
        series_2.setName("NFT 2")
        series_2.append(1.25*60*60*1000, 5.32)
        series_2.append(2.5*60*60*1000, 1.76)
        series_2.append(3.125*60*60*1000, 8.20)
        series_2.append(4.75*60*60*1000, 9.77)

        # Aufgabe 3
