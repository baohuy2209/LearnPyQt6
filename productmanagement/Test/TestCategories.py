from productmanagement.libs.JSF import jsonfilefactory
from productmanagement.models.Category import Category

categories=[]
categories.append(Category("c1","catel1"))
categories.append(Category("c2","catel2"))
categories.append(Category("c3","catel3"))
categories.append(Category("c4","catel4"))
categories.append(Category("c5","catel5"))
categories.append(Category("c6","catel6"))
categories.append(Category("c7","catel7"))
categories.append(Category("c8","catel8"))
categories.append(Category("c9","catel9"))
categories.append(Category("c10","catel10"))
categories.append(Category("c11","catel11"))
categories.append(Category("c12","catel12"))
print("List of Categories:")
for c in categories:
    print(c)

filename="../dataset/categories.json"
jff=jsonfilefactory()
jff.write_data(categories,filename)