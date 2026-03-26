import json
import random
from prettytable import PrettyTable
from product import Product
from sale import Sale
from datetime import datetime
products=[]
sales=[]

def LoadFromFile():
    with open('products.json','r')as f:
        json_list=json.load(f)
        for json_item in json_list:
            p=Product.fromjson(json_item)
            products.append(p)
def saveToFile():
    #json_list=[]#for p in products:json_list.append(p.tojson())
    json_list=list(map(lambda p:p.tojson(),products))
    with open ('products.json','w') as f:json.dump(json_list,f,indent=4)
            
def ViewAllProducts():
    print("View Our Products")
    table=PrettyTable()
    table.field_names=["ID","Name","Price","Stock"]
    for p in products:table.add_row([p.id,p.name,p.price,p.stock])
    table.align="l"
    print(table)
def shopping():
    print("Enjoy your shopping")
    print("------------------------")
    pid_list=list(map(lambda p:p.id,products))
    pick_items=[] #[(),(),()]
    name=input("Enter your name:")
    while True:
        print(f"\nHi {name}.Which product do you want to buy?")
        pid=int(input('Enter the shopping ID of the product:'))
        while pid not in pid_list:
            print('Invalid Error! Try Again')
            pid=int(input('Enter your shopping ID:'))
        p=products[pid_list.index(pid)]
        print(f"How much {p.name}s do you want to buy?")
        count=int(input("Enter count:"))
        while count>p.stock:
            print(f"Sorry! Insufficient stock! We only have {p.stock}")
            count=int(input("Enter count:"))
        item=(p.name,count,count*int(p.price))
        pick_items.append(item)  #pick_items[key]=value
        ans=input("Check out now? Y/N:").lower()
        if ans=='y':break
    check_out(name,pick_items)
def check_out(name,pick_items):
    print("Your Check Out")
    print("----------------------")
    print("Customer Name:",name)
    table=PrettyTable()
    table.field_names=["Products","Count","Sub Total"]
    total=0
    for item in pick_items:  #item as tuple (name,count,sub total)
        table.add_row(item)
        total+=item[2]
    table.add_row(["","Total",total])
    table.align="l"
    print(table)
    ans=input("Type 'confirm' to complete your sales:").lower()
    if ans=='confirm':
        AddNewSaleToFile(name,total)
        updateProducts(pick_items)
    else: print("You cancelled the sale.")
    
def LoadSalesFromFile():
    try:
        with open('sales.json','r')as f:
            json_list=json.load(f)
            for json_item in json_list:
                s=Sale.fromJson(json_item)
                sales.append(s)
    except FileNotFoundError: pass
def AddNewSaleToFile(name,total):
    json_sales_list=list(map(lambda s:s.toJson(),sales))
    json_sales_list.append(
        {
            'id':random.randint(1000,9999),
            'name':name,
            'total':total,
            'date':datetime.now().strftime('%d-%m-%y')
            }
    )
    with open('sales.json','w') as f: json.dump(json_sales_list,f,indent=4)
    print("Thank for shopping with us")
def updateProducts(pick_items):  #list of tuple (name,count,sub total)
    for item in pick_items:
        item_name=item[0]
        item_count=item[1]
        for i in range(len(products)):
            if products[i].name==item_name:
                products[i].stock-=item_count
                break
    saveToFile()
    
def run():
    LoadFromFile()   #initialize the products[]
    LoadSalesFromFile()
    ViewAllProducts()
    shopping()
    