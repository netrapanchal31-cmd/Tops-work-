Data = {}

def add_fruit(data):
    name = input("Enter fruit name: ").lower()
    quantity = int(input("Enter quantity: "))
    price = int(input("Enter price: "))

    data[name] = {'price': price, 'quantity': quantity}
    print("Fruit added successfully ")


def view_stock(data):
    if not data:
        print("No fruits available ")
    else:
        for fruit, details in data.items():
            print(f"Fruit: {fruit}, Price: {details['price']}, Quantity: {details['quantity']}")


def update_stock(data):
    name = input("Enter fruit name: ").lower()

    if name not in data:
        print("Fruit not found ")
    else:
        quantity = int(input("Enter new quantity: "))
        price = int(input("Enter new price: "))

        data[name] = {'price': price, 'quantity': quantity}

        print("Fruit updated successfully ")