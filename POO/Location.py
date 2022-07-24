
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        
    def myLocation(self):
        print("Hola mi nombre es  " + self.name + " y vivo en " + self.country + ".")
    
    
loc1 = Location("Hugo", "Colombia")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")

print(loc1.name, loc2.name, loc3.name)
print(loc1.country, loc2.country, loc3.country)
print(type(loc1))
print(type(loc2))
print(type(loc3))

loc1.myLocation()
loc2.myLocation()
loc3.myLocation()