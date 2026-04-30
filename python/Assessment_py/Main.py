import json

def load_data():
    try:
        with open("fruits.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("fruits.json", "w") as file:
        json.dump(data, file)


from Part_1_Manager import add_fruit, view_stock, update_stock
from part_2_customer import buy_fruit


def main():
    data = load_data()

    while True:
        print("\nWELCOME TO FRUIT MARKET")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            while True:
                print("\n--- Manager Menu ---")
                print("1. Add Fruit")
                print("2. View Stock")
                print("3. Update Stock")
                print("4. Back")

                m_choice = input("Enter choice: ")

                if m_choice == "1":
                    add_fruit(data)
                elif m_choice == "2":
                    view_stock(data)
                elif m_choice == "3":
                    update_stock(data)
                elif m_choice == "4":
                    break
                else:
                    print("Invalid choice")

        elif choice == "2":
            while True:
                print("\n--- Customer Menu ---")
                print("1. View Stock")
                print("2. Buy Fruit")
                print("3. Back")

                c_choice = input("Enter choice: ")

                if c_choice == "1":
                    view_stock(data)
                elif c_choice == "2":
                    buy_fruit(data)
                elif c_choice == "3":
                    break
                else:
                    print("Invalid choice")

        elif choice == "3":
            print("Thank you! ")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()