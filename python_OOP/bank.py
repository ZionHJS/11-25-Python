class BankAccount:
	def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
        if amount > self.balance:
            print('insufficient funds:Chargin a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
	def display_account_info(self):
		print(f'Balance:{self.balance}')
	def yield_interest(self):
		self.balance*(1+self.int_rate)
        return self.balance

mikeBank = BankAccount(0.08, 10000)