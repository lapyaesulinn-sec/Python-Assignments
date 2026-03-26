class Product:
    def __init__(self,id,name,price,stock):
        self.id,self.name,self.price,self.stock=id,name,price,stock
    def fillStock(self,new_stock):
        self.stock+=new_stock
    def tojson(self):
        return{
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'stock':self.stock}
    @staticmethod
    def fromjson(json):
        return Product(json['id'],json['name'],json['price'],json['stock'])
        
