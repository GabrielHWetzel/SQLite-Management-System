import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QDialog, QWidget,\
    QLabel, QLineEdit, QPushButton, QTableWidget
from PyQt6.QtGui import QAction


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

    def load_data(self):
        self.table
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
