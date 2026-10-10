# polymorphism 2

class Bird:
    
    def fly(self):
        print("Bird can fly")

class Eagle(Bird):
    
    def fly(self):
        print("Eagle files at a high latitude")
        
class Penguin(Bird):
    
    def fly(self):
        print("penguin can't fly, it swims instead")
        
#polymorphism in action
def make_it_fly(bird):
    bird.fly()
    

#create object
eagle = Eagle()
penguin = Penguin()

# use the same interface (make_it_fly) for different object

make_it_fly(eagle)
make_it_fly(penguin)