# Class 

class product:
    # method
    # attribute, property 
    def __init__(self, name, price, isActive): # constructor sınıf çağrıldığında otomatik olarak çalışır.
        self.name = name
        self.price = price
        self.isActive = isActive
    # instance method

    def intro(self):
        return f"{self.name} - {self.price}"
    

# instanca, object

p1 = product("iphone 15", 50000, True)
p2 = product("iphone 14", 40000, True)
p3 = product("iphone 13", 30000, False)
    
urunler = [p1,p2,p3]

for urun in urunler:
    if urun.isActive:
        print(urun.intro())
        # print(f"{urun.name} - {urun.price}")