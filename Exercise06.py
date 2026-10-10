# creating a getter property and setter property

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.__email = email # private variable
        self.password = password
        
    @property
    def email(self):
        print("Email accessed")
        return self.__email
    
    @email.setter
    def email(self,new_email):
        self.__email = new_email

user1 = User("kamal","ksiri@gmail.com","ksiri1234")

print(user1.email)


user1.email = "kamal@gmail.com"

print(user1.email)
        