from productmanagement.libs.JSF import jsonfilefactory
from productmanagement.models.Category import Category
from productmanagement.models.Product import Product


class dataconnector:
    def get_all_categories(self):
        self.categories = []
        self.jff = jsonfilefactory()
        c_filename = "../dataset/categories.json"
        self.categories = self.jff.read_data(c_filename, Category)
        return self.categories
    def get_all_products(self):

        self.products = []
        self.jff = jsonfilefactory()
        p_filename = "../dataset/products.json"
        self.products = self.jff.read_data(p_filename, Product)
        return self.products
    def get_products_by_cateid(self,cateid):
        self.jff = jsonfilefactory()
        p_filename = "../dataset/products.json"
        self.products = self.jff.read_data(p_filename, Product)
        products_tmp = []
        for p in self.products:
            if p.cateid == cateid:
                products_tmp.append(p)
        self.products = products_tmp
        return self.products
    def save_product(self,p):
        self.products=self.get_all_products()
        self.products.append(p)
        filename = "../dataset/products.json"
        jff = jsonfilefactory()
        jff.write_data(self.products, filename)
    def find_index(self,proid):
        self.products = self.get_all_products()
        for i in range (len(self.products)):
            p=self.products[i]
            if p.proid==proid:
                return i
        return -1
    def update_product(self,product):
        index=self.find_index(product.proid)
        if index!=-1:
            self.products[index]=product
            filename = "../dataset/products.json"
            jff = jsonfilefactory()
            jff.write_data(self.products, filename)
    def delete_product(self,proid):
        index=self.find_index(proid)
        if index!=1:
            self.products.pop(index)
            filename = "../dataset/products.json"
            jff = jsonfilefactory()
            jff.write_data(self.products, filename)




