import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog


class CSVReaderApp(QMainWindow):
    def __init__(self):
        super(CSVReaderApp, self).__init__()

        self.setWindowTitle("CSV Reader App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.table_widget = QTableWidget(self)
        self.layout.addWidget(self.table_widget)

        self.load_button = QPushButton("Load CSV", self)
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)

    def load_csv(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_name:
            # Read CSV file using pandas
            df = pd.read_csv(file_name)

            # Display data in the table widget
            self.display_data(df)

    def display_data(self, dataframe):
        self.table_widget.clear()

        # Set column and row count
        self.table_widget.setRowCount(dataframe.shape[0])
        self.table_widget.setColumnCount(dataframe.shape[1])

        # Set column headers
        self.table_widget.setHorizontalHeaderLabels(dataframe.columns)

        # Populate the table with data
        for row in range(dataframe.shape[0]):
            for col in range(dataframe.shape[1]):
                item = QTableWidgetItem(str(dataframe.iat[row, col]))
                self.table_widget.setItem(row, col, item)

        # Resize columns to fit the content
        self.table_widget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVReaderApp()
    window.show()
    sys.exit(app.exec_())
