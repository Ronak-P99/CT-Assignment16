from book import Book

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, status):
        if item.name in self.items:
            self.items[item.name['status']] = status
        else:
            self.items[item.name] = {'book': item, 'status': status}

    def view_cart(self):
        for item_name, details in self.items.items():
            item, status = details['book'], details['status']
            print(f"{item_name} - {item.author} -  ${item.price} - {status}")
    
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from the cart")
        else:
            print("Book not found in the cart")

    def checkout(self):
        total = sum(item['book'].price for item in self.items.values())
        print(f"Total amount: ${total}")
        self.items = {}
        print("Checkout successful!")
