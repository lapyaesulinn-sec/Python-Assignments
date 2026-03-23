import json
from product import Product
import random
products=[]
def displayMenu():
    print('Shop Menu')
    print('----------')
    print('1. View Product')
    print('2. Add Product')
    print('3. Fill Stock')
    print('4. Delete Stock')
    print('5. View Selling List')
    print('q. Quit')
def saveToFile():
    #json_list=[]
    #for p in products:json_list.append(p.tojson())
    json_list=list(map(lambda p:p.tojson(),products))
    with open ('products.json','w') as f:json.dump(json_list,f,indent=4)
def AddNewProduct():
    print('Add New Product')
    print('-------------------')
    id=random.randint(1000,9999)
    print(f'id\t:{id}')
    name=input('name\t:')
    price=input('price\t:')
    stock=input('stock\t:')
    p=Product(id,name,price,stock)
    products.append(p)
    saveToFile()
    print('New Product added successfully')

while True:
    displayMenu()
    ans=input('Your answer:')
    if ans=='1':pass
    elif ans=='2':AddNewProduct()