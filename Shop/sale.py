class Sale:
    def __init__(self,id,name,total,date):
        self.id,self.name,self.total,self.date=id,name,total,date
    
    def toJson(self):
        return{
            'id':self.id,
            'name':self.name,
            'total':self.total,
            'date':self.date
            }
    @staticmethod
    def fromJson(json):
        return Sale(json['id'],json['name'],json['total'],json['date'])