import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QDialog, QWidget, \
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, \
    QToolBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Title
        self.setWindowTitle("Student Management System")

        # Size
        self.setMinimumSize(440, 500)

        # Menu Items
        file_menu_item = self.menuBar().addMenu("&File")
        edit_menu_item = self.menuBar().addMenu("&Edit")
        help_menu_item = self.menuBar().addMenu("&Help")

        # File Menu
        add_student_action = QAction(QIcon("icons/add.png"),"Add Student", self)
        add_student_action.triggered.connect(self.add_student)
        file_menu_item.addAction(add_student_action)

        # Edit Menu
        search_action = QAction(QIcon("icons/search.png"),"Search", self)
        search_action.triggered.connect(self.search_student)
        edit_menu_item.addAction(search_action)

        # Help Menu
        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        help_menu_item.addAction(about_action)

        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Main Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        self.load_data()

        # Status bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def cell_clicked(self):
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.edit_student)
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_student)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def add_student(self):
        dialog = InsertDialog()
        dialog.exec()

    def search_student(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit_student(self):
        dialog = EditDialog()
        dialog.exec()

    def delete_student(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        pass




class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle("Add Student")
        self.setFixedSize(300, 150)

        # Student Information
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")

        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)

        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("Phone Number")

        # Submit
        submit = QPushButton("Submit")
        submit.clicked.connect(self.add_student)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.student_name)
        layout.addWidget(self.course_name)
        layout.addWidget(self.mobile_number)
        layout.addWidget(submit)
        self.setLayout(layout)

    def add_student(self):

        # Get Values
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()

        # Insert into Database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()

        # Refresh
        window.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle("Search Student")
        self.setFixedSize(300, 150)

        # Student Information
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")

        # Search
        search = QPushButton("Search")
        search.clicked.connect(self.search_student)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.student_name)
        layout.addWidget(search)
        self.setLayout(layout)

    def search_student(self):

        # Get Student
        name = self.student_name.text()

        # Get Values from database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name=?", (name,))

        # Display Selection on Table
        items = window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            window.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle("Edit Student")
        self.setFixedSize(300, 150)

        # Student Information
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")

        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)

        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("Phone Number")

        # Submit
        submit = QPushButton("Submit")
        submit.clicked.connect(self.edit_student)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.student_name)
        layout.addWidget(self.course_name)
        layout.addWidget(self.mobile_number)
        layout.addWidget(submit)
        self.setLayout(layout)


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
