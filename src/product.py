class Product:
    weight = 0
    price = 0
    id = 0;

    def __init__(self, id ,weight, price):
        self.id = id
        self.weight = weight
        self.price = price
    
    def __str__(self):
        return "ID: "+str(self.id)+"\n Waga:"+str(self.weight)+"\nCena: "+str(self.price)
   
    def __repr__(self):
        return "\nID: "+str(self.id)+"\nWaga:"+str(self.weight)+"\nCena: "+str(self.price)+"\n"