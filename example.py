import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QGridLayout, \
    QLabel, QWidget, QLineEdit, QPushButton


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # Widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_label = QLabel("Date of Birth: (MM/DD/YYYY)")
        self.date_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        self.output_label = QLabel("")

        # Grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.date_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        current_time = datetime.now().year
        date_of_birth = self.date_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        calculated = current_time - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {calculated} years old.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
