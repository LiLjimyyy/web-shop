class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price

    def search_by_name(products, text):
        return [p for p in products if text.lower() in p.name.lower()]