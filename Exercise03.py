# Accessing and modifying object data

class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
        
    def say_hi_to_user(self,user):
        print(f"Sending massage to {user.username}: Hi {user.username},it's {self.username}")
        
        
user1 = User("spiderman","spidy@gmail.com","1@34")
user2 = User("Batman","BatM@gmail.com","Bat@34")



user1.say_hi_to_user(user2)  
user2.say_hi_to_user(user1)

print(user1.email)
user1.email = "Danyy@gmail.com"
print(user1.email)

