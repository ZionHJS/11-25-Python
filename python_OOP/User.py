class User:
    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance
        
    def make_withdrawwal(self, amount):
        print(self.balance)
        self.balance -= amount
        print('after withdraw', self.balance)
        
    def display_user_balance(sef):
        print(f'User:{self.name}', f'Balance:{self.balance}')

    def transfer_money(self, other_user, amount):
        