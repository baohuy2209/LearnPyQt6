from PyQt6.QtWidgets import QApplication, QMainWindow

from LearnQDateEdit.ui.FoodManagementExt import FoodManagementExt

app = QApplication([])
myWindow = FoodManagementExt()
MainWindow = QMainWindow()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()
