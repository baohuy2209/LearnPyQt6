class Product:
    def __init__(self, ProductId, ProductName, Price, ExpiredDate, FreeTax):
        self.ProductId = ProductId
        self.ProductName = ProductName
        self.Price = Price
        self.ExpiredDate = ExpiredDate
        self.FreeTax = FreeTax
    def __str__(self):
        return str(self.ProductId) + " - " + self.ProductName
