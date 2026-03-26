import json
from customer import sales
from product import Product
import random
from prettytable import PrettyTable
from sale import Sale
products=[]
sales=[]
def LoadSalesFromFile():
    try:
        with open('sales.json','r')as f:
            json_list=json.load(f)
            for json_item in json_list:
                s=Sale.fromJson(json_item)
                sales.append(s)
    except FileNotFoundError: pass

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
    #json_list=[]#for p in products:json_list.append(p.tojson())
    json_list=list(map(lambda p:p.tojson(),products))
    with open ('products.json','w') as f:json.dump(json_list,f,indent=4)
def AddNewProduct():
    print('Add New Product')
    print('-------------------')
    id=random.randint(1000,9999)
    print(f'id\t:{id}')
    name=input('name\t:')
    price=input('price\t:')
    stock=int(input('stock\t:'))
    p=Product(id,name,price,stock)
    products.append(p)
    saveToFile()
    print('New Product added successfully')
def ViewProduct():
    print("All Products")
    table=PrettyTable()
    table.field_names=["ID","Name","Price","Stock"]
    for p in products:table.add_row([p.id,p.name,p.price,p.stock])
    table.align="l"
    print(table)
def LoadFromFile():
    with open('products.json','r')as f:
        json_list=json.load(f)
        for json_item in json_list:
            p=Product.fromjson(json_item)#from json to object form
            products.append(p)
def FillStock():
    print("Fill New Stock:")
    print("--------------------")
    pid_list=list(map(lambda p:p.id,products))
    pid=int(input("Enter New Stock:"))
    while pid not in pid_list:
        print("Invalid Number! Try Again")
        pid=int(input("Enter New Stock"))
    found_index=pid_list.index(pid)
    chosen_p=products[found_index]
    print("Chosen products\t:",chosen_p.name)
    new_stock=int(input("Enter New Stock:"))
    chosen_p.fillStock(new_stock)
    products[found_index]=chosen_p
    saveToFile()
    print(f"{new_stock} Stocks added to {chosen_p.name} successfully")
def deleteProduct():
    print("Delete Product")
    print('-----------------')
    pid_list=list(map(lambda p:p.id,products))
    pid=int(input("Enter Product ID:"))
    while pid not in pid_list:
        print("Invalid Number! Try Again")
        pid=int(input("Enter Product ID:"))
    found_index=pid_list.index(pid)
    chosen_p=product[found_index]
    print("Selected Product:",chosen_p.name)
    confirm=input("Are you sure to delete? Y/N:").lower()
    if confirm=='y':
        products.remove(chosen_p)
        saveToFile()
        print(f'{chosen_p.name} is deleted successfully')
    else:print("Cancelled")
def viewAllSales():
    table=PrettyTable()
    table.field_names=['ID','Customer Name','Total','Date']
    for sale in sales:
        table.add_row([sale.id,sale.name,sale.total,sale.date])
    table.align="l"
    print(table)
def run():
    LoadFromFile()
    LoadSalesFromFile()
    while True:
        displayMenu()
        ans=input('Your answer:')
        if ans=='1':ViewProduct()
        elif ans=='2':AddNewProduct()
        elif ans=='3':FillStock()
        elif ans=='4':deleteProduct()
        elif ans=='5':viewAllSales()
        elif ans=='q':break
        else:print('Invalid Answer!Try Again')
        