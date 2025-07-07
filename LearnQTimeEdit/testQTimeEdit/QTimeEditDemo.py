import sys

from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QWidget, QFormLayout, QTimeEdit, QLabel, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt QTimeEdit")
        self.setMinimumWidth(200)
        layout = QFormLayout()
        self.setLayout(layout)

        self.time_edit = QTimeEdit(self)
        time = QTime(10, 15, 35)
        self.time_edit.setTime(time)
        self.time_edit.setDisplayFormat("HH:mm:ss A")

        self.time_edit.editingFinished.connect(self.update_time)
        self.time_edit.timeChanged.connect(self.change_time)
        self.result_label = QLabel('', self)

        layout.addRow('Time:', self.time_edit)
        layout.addRow(self.result_label)
    def update_time(self):
        value = self.time_edit.time()
        print(str(value.toPyTime()))
        self.result_label.setText(str(value.toPyTime()))
        pass
    def change_time(self):
        value = self.time_edit.time()
        print(str(value.toPyTime()))
        self.result_label.setText(str(value.toPyTime()))
app = QApplication([])
window = MainWindow()
window.show()
app.exec()