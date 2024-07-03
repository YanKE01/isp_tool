from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QHBoxLayout


class CCMParameter:
    def __init__(self):
        super().__init__()
        self.data = []

    def loadFromTable(self, table_widget: QTableWidget) -> list:
        self.data = []
        rows = table_widget.rowCount()
        columns = table_widget.columnCount()
        for row in range(rows):
            for column in range(columns):
                item = table_widget.item(row, column)
                try:
                    value = float(item.text()) if item else 0.0
                except ValueError:
                    value = 0.0
                self.data.append(value)
        return self.data

    def showTable(self) -> None:
        print(f"ccm parameter:{self.data}")
