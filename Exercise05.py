# Getters and Setter

from datetime import datetime

class User:
    def __init__(self,username,email,password):
        self.username = username
        self.__email = email
        self.password = password
        
    def get_email(self):
        print(f"now time is : {datetime.now()}")
        return self.__email
    
    def set_email(self,new_email):
        if "@" in new_email:
            self.__email = new_email
    
    
user1 = User("jonny","jonny@gmail.com","j@123")


print(user1.get_email()) 

user1.set_email("jsins@gmail.com")

print(user1.get_email())  

user1.set_email("jsinsgmail.com")

print(user1.get_email())  