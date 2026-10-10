# Encapsulation

class Person:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        
    @property
    def GetName(self):
        return self.__name
    
    @GetName.setter
    def SetName(self,value):
        self.__name = value
        
    @staticmethod
    def mymethod():
        print("your succussfully Login....")
        
        
p1 = Person("nimal",22,"male")

print(p1.GetName)

p1.SetName = "kusal"
print(p1.GetName)

Person.mymethod()  # static method not have object we can static method use direct class called



