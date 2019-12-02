#Attributes
class User:
    def __init__(self):
        self.name = 'Michael'
        self.email = 'michael@codingdojo.com'
        self.account_balance = 0
#instantiate couple of new users
guido = User()
monty = User()
#access instance's attributes
print(guido.name)
print(monty.name)
#set values for our instance's attributes
guido.name = 'Guido'
monty.name = 'Monty'

#adjust the code to allow arguments to be passed in upon instantiation
#using the __init__ methods paramenters to indicate what needs to be provided
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
#create user with each arguments
guido = User('Guido van Rassum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
print(guido.name)
print(monty.name)



#Methods: functions that belongs to the class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accout_balance = 0
    #the first parameter of every method within a class should be self
    def make_deposit(self, amount):
        self.account_balance += amount

guido = User()
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
print(guido.account_balance)
print(monty.account_balance)

#self: the parameter includes all the information about the individual object that has called the method
