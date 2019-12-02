class store:
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = ''
    
class product:
    def __init__(self, price, category):
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price*(1+percent_change)
        else:
            self.price = self.price*(1-percent_change)
