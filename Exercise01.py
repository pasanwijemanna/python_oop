# creating classes and objects , combining objects

class Dog:
    def __init__(self,name,breed , owner):
        self.name = name
        self.breed = breed
        self.owner = owner   
        
    def bark(self):
        print("Whoof Whoof")
        
        
class Owner:
    def __init__(self,name,address, contact_number):
        self.name = name
        self.address =address
        self.phone_number = contact_number


owner1 = Owner("Nimal","98,Temple road,Kaduwela","0112456789")        
dog1 = Dog("Timy","great dane",owner1)   # combining object 
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

owner2 = Owner("Sandi","102,udahamulla road,wallampitiya","0113456789")
dog2 = Dog("Ruby","Labrodor",owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.name)











