from cart import ShoppingCart, Book

def main():
    cart = ShoppingCart()
    while True:
        try:
            action = input("Choos action: add, remove, view, checkout: ")
            if action not in ['add', 'remove', 'view', 'checkout']:
                raise ValueError("Invalid action.")
            if action == 'add':
                name = input("Enter book name: ")
                author = input("Enter author name: ")
                price = float(input("Enter book price: "))
                status = 'available'
                cart.add_item(Book(name, author, price), status)
            elif action == 'remove':
                name = input("Enter book name to remove: ")
                cart.remove_item(name)
            elif action == 'view':
                cart.view_cart()
            elif action == 'checkout':
                cart.checkout()
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()