from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem, QMessageBox

from productmanagement.libs.dataconnector import dataconnector
from productmanagement.models.Product import Product
from productmanagement.ui.ProductMainWindow import Ui_MainWindow


class ProductMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dc=dataconnector()
        self.categories=[]
        self.products=[]
        self.categories=self.dc.get_all_categories()
        self.products=self.dc.get_all_products()
        self.selected_cate=None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.show_categories_ui()
        self.show_products_ui()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def show_categories_ui(self):
        self.listWidgetCategory.clear()
        for c in self.categories:
            citem=QListWidgetItem(str(c))
            self.listWidgetCategory.addItem(citem)

    def show_products_ui(self):

        self.tableWidgetProduct.setRowCount(0)
        for p in self.products:
            row=self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)
            #Tao cot ma:
            col_id=QTableWidgetItem(p.proid)
            col_name=QTableWidgetItem(p.proname)
            col_price=QTableWidgetItem(str(p.price))
            col_quantity=QTableWidgetItem(str(p.quantity))
            col_cateid=QTableWidgetItem(p.cateid)

            self.tableWidgetProduct.setItem(row,0,col_id)
            self.tableWidgetProduct.setItem(row,1,col_name)
            self.tableWidgetProduct.setItem(row,2,col_price)
            self.tableWidgetProduct.setItem(row,3,col_quantity)
            self.tableWidgetProduct.setItem(row,4,col_cateid)
            if p.price>=300 and p.price<=500:
                col_id.setBackground(Qt.GlobalColor.red)
                col_name.setBackground(Qt.GlobalColor.red)
                col_price.setBackground(Qt.GlobalColor.red)
                col_quantity.setBackground(Qt.GlobalColor.red)
                col_cateid.setBackground(Qt.GlobalColor.red)

    def setupSignalAndSlot(self):
        self.listWidgetCategory.itemSelectionChanged.connect(self.process_cate_selection)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.show_product_detail)
        self.pushButtonClear.clicked.connect(self.clear_detail_infor)
        self.pushButtonSave.clicked.connect(self.save_product)
        self.pushButton_3.clicked.connect(self.delete_product)

    def process_cate_selection(self):
        index=self.listWidgetCategory.currentRow()
        if index<0:
            return
        self.selected_cate=self.categories[index]
        self.products=self.dc.get_products_by_cateid(self.selected_cate.cateid)
        self.show_products_ui()
    def show_product_detail(self):
        index=self.tableWidgetProduct.currentRow()
        if index<0:
            return
        product=self.products[index]
        self.lineEditProductID.setText(product.proid)
        self.lineEditProductName.setText(product.proname)
        self.lineEditUnitPrice.setText(str(product.price))
        self.lineEditQuantity.setText(str(product.quantity))
        self.lineEditCateID.setText(product.cateid)
    def clear_detail_infor(self):
        self.lineEditProductID.clear()
        self.lineEditProductName.clear()
        self.lineEditUnitPrice.clear()
        self.lineEditQuantity.clear()
        self.lineEditCateID.clear()
        self.lineEditProductID.setFocus()
    def save_product(self):
        #Step1: Create a Product object:
        p=Product()
        p.proid=self.lineEditProductID.text()
        p.proname=self.lineEditProductName.text()
        p.price=float(self.lineEditUnitPrice.text())
        p.quantity=int(self.lineEditQuantity.text())
        p.cateid=self.lineEditCateID.text()
        #step 2: save product into json database
        index=self.dc.find_index(p.proid)
        if index==-1:
            self.dc.save_product(p)
        else:
            self.dc.update_product(p)
        self.dc.save_product(p)
        #step 3
        if self.selected_cate!=None:
            self.products=self.dc.get_products_by_cateid(self.selected_cate.cateid)
        else:
            self.products = self.dc.get_products_by_cateid(self.selected_cate.cateid)
        self.show_products_ui()
    def delete_product(self):
        proid = self.lineEditProductID.text()
        msg=QMessageBox(self.MainWindow)
        msg.setText("Muon xoa sp["+proid+"] ha?")
        msg.setWindowTitle("xac nhan xoa")
        buttons=QMessageBox.standardButton.Yes|QMessageBox.standardButton.No
        msg.setStandardButtons(buttons)
        if msg.exec()==QMessageBox.StandardButton.No:
            return #ko xoa
        self.dc.delete_product(proid)
        # step 3
        if self.selected_cate != None:
            self.products = self.dc.get_products_by_cateid(self.selected_cate.cateid)
        else:
            self.products = self.dc.get_products_by_cateid(self.selected_cate.cateid)
        self.show_products_ui()
    def exit_program(self):
        