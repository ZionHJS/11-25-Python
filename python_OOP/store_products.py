class store:
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = []
    def add_products(self, new_product):
        self.list_products.append(new_product)
    def sell_product(self, id):
        self.list_products.remove(list_products[id])
    def inflation(self, percent_increase):
    
    def set_clearance(self, category, percent_discount):
        
    
class product:
    def __init__(self, price, category):
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price*(1+percent_change)
        else:
            self.price = self.price*(1-percent_change)
    def print_info(self):
        print(f'{self.name}', f'{self.category}', f'{self.price}')
