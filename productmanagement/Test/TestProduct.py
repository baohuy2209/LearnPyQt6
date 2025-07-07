import random

from productmanagement.libs.JSF import jsonfilefactory
from productmanagement.models.Product import Product

products=[]
n=1000
for i in range(1,n+1):
    cateid=random.randrange(1,13)
    price=random.randrange(100,500)
    quantity=random.randrange(1,20)
    products.append(Product(f"p{i}",f"Product {i}",price, quantity,f"c{cateid}"))
print("List of Products:")
for p in products:
    print(p)
filename="../dataset/products.json"
jff=jsonfilefactory()
jff.write_data(products,filename)