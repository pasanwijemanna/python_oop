# Access modifiers:protected attributes  and private attibutes

class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email  # protected attribute
        self.__password = password # private attribute
        
    def get_email(self):
        return self._email
    
    def get_passcode(self):
        return self.__password
        
        
user1 = User("spiderman","spidy@gmail.com","1@34")


print(user1.get_email())

print(user1._email)


print(user1.get_passcode())