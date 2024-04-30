import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QDialog, QWidget,\
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Student Management System")

        # Items
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        # File menu
        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        # Help menu
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.setCentralWidget(self.table)

        self.load_data()

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
