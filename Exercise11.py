# Abstraction

from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    def __init__(self,n):
        self.no_of_tyers = n
        
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
     def __init__(self,n,color):
         super().__init__(n)
         self.color = "Black"
        
     def start(self):
        print("start with kick")
          
class Scooty(Vehicle):
    def __init__(self,n):
        self.no_of_tyers = n 
    
    def start(self):
        print("self start")
        
class Car(Vehicle):
    def __init__(self,n):
        self.no_of_tyers = n 
        
    def start(self):
        print("start with key")   


bike1 = Bike(2,"Black")
print(bike1.no_of_tyers)
print(bike1.color)
bike1.start()

car1 = Car(4)
print(car1.no_of_tyers)
car1.start()

scooty1 = Scooty(2)
print(scooty1.no_of_tyers)
scooty1.start()

