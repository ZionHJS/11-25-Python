class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line


class User:
    # other methods
    def make_deposit(self, amount):
    	self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore

class User:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        if amount > self.account_balance:
            print('insuffficcient acount_balance')
        else:
            self.account_balance -= amount
    def display_user_balance(self):
        print(f'{self.account_balance}')
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    	print(self.account.balance)		# or access its attributes