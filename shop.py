class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price

def find_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]

def apply_discount(price, percent):
    return price * (100 - percent) / 10

def add_tax(price, rate=0.09):
    return price * (1 + rate)

def apply_coupon(price):
    return price - 5

# note
# one
# two
# wip 1
# wip 2
# Agi
# A
# in progress

def search_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]
