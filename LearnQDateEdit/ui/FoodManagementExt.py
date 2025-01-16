from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox

from LearnQDateEdit.io.FileFactory import FileFactory
from LearnQDateEdit.models.Product import Product
from LearnQDateEdit.ui.FoodManagement import Ui_MainWindow
import datetime

class FoodManagementExt(Ui_MainWindow):
    def __init__(self):
        self.arrData = []
        self.fileFactory = FileFactory()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.arrData = self.fileFactory.readData("database.json", Product)
        self.showProductIntoQListWidget()
        self.setupSignAndSlots()
        self.listWidgetListProduct.itemSelectionChanged.connect(self.processItemSelection)
    def setupSignAndSlots(self):
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonDelete.clicked.connect(self.processDelete)
    def processItemSelection(self):
        row = self.listWidgetListProduct.currentRow()
        item = self.listWidgetListProduct.item(row)
        product = item.data(Qt.ItemDataRole.UserRole)
        self.lineEditID.setText(str(product.ProductId))
        self.lineEditName.setText(product.ProductName)
        self.lineEditPrice.setText(str(product.Price))
        if isinstance(product.ExpiredDate, str):
            product.ExpiredDate = datetime.date.fromisoformat(product.ExpiredDate)
        self.dateEdit.setDate(product.ExpiredDate)
        if product.FreeTax:
            self.checkBoxFreeTax.setCheckState(Qt.CheckState.Checked)
        else:
            self.checkBoxFreeTax.setCheckState(Qt.CheckState.Unchecked)
    def processDelete(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidgetListProduct.count()):
            item = self.listWidgetListProduct.item(index)
            if item.checkState() == Qt.CheckState.Checked:
                product = item.data(Qt.ItemDataRole.UserRole)
                self.arrData.remove(product)
        self.showProductIntoQListWidget()
        self.fileFactory.writeData("database.json", self.arrData)
    def processNew(self):
        self.lineEditID.setText("")
        self.lineEditName.setText("")
        self.lineEditPrice.setText("")
        self.checkBoxFreeTax.setCheckState(Qt.CheckState.Unchecked)
        self.lineEditID.setFocus()
    def checkDuplicate(self, id):
        items = [x for x in self.arrData if x.ProductId == id]
        if len(items) == 0:
            return None
        return items[0]
    def processSave(self):
        id = self.lineEditID.text()
        name = self.lineEditName.text()
        price = float(self.lineEditPrice.text())
        date = self.dateEdit.date().toPyDate()
        freeTax = self.checkBoxFreeTax.isChecked()
        newItem = Product(id, name, price, date, freeTax)
        oldItem=self.checkDuplicate(id)
        if oldItem != None:
            index = self.arrData.index(oldItem)
            self.arrData[index] = newItem
        else:
            self.arrData.append(newItem)
        self.showProductIntoQListWidget()
        self.fileFactory.writeData("database.json", self.arrData)
    def showProductIntoQListWidget(self):
        self.listWidgetListProduct.clear()
        for product in self.arrData:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, product)
            item.setText(str(product))
            item.setCheckState(Qt.CheckState.Unchecked)
            if product.FreeTax == True:
                item.setIcon(QIcon("images/tax.png"))
            else:
                item.setIcon(QIcon("images/tax_including.png"))
            if isinstance(product.ExpiredDate, str):
                product.ExpiredDate = datetime.date.fromisoformat(product.ExpiredDate)
            day = (product.ExpiredDate - datetime.date.today()).days
            if day <= 7:
                item.setForeground(Qt.GlobalColor.red)
            self.listWidgetListProduct.addItem(item)
    def show(self):
        self.MainWindow.show()