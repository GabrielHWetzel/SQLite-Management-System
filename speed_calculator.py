import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, \
    QWidget, QLabel, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        self.unit_combo_box = QComboBox()
        self.unit_combo_box.addItems(['Metric (km)', 'Imperial (mi)'])

        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        self.calculated_label = QLabel("")

        # Grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit_combo_box, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 1)

        grid.addWidget(self.calculated_label, 4, 0, 1, 3)

        self.setLayout(grid)

    def calculate(self):
        distance = int(self.distance_line_edit.text())
        time = int(self.time_line_edit.text())
        average_speed = distance / time

        match self.unit_combo_box.currentText():
            case 'Metric (km)':
                unit_type = "km"
            case 'Imperial (mi)':
                unit_type = "mi"

        self.calculated_label.setText(f"Average Speed: {average_speed} {unit_type}/h")


app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())
