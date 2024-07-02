from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QHBoxLayout


class CcmTableData:
    def __init__(self):
        super().__init__()
        self.data = []

    def load_from_table(self, table_widget: QTableWidget) -> list:
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


    def show_table_data(self) -> None:
        # 打印表格数据并添加行和列标签
        headers = ["R", "G", "B"]
        header_str = "    " + "  ".join(f"{h:^6}" for h in headers)  # 列标签居中对齐
        print(header_str)
        for i, row in enumerate(self.data):
            row_label = headers[i]
            row_str = f"{row_label:^3}  " + "  ".join(f"{value:^6.2f}" for value in row)  # 行标签和行数据居中对齐
            print(row_str)