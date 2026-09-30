print("*"*38)
print("            RESTAURANT")
print("         MANAGEMENT SYSTEM")


# CUSTOMER DETAIL FUNCTION


def get_customer_details():

    print("\n          CUSTOMER DETAILS")

    name = input("Enter Customer's name: ")
    table = input("Enter Table number: ")

    return name, table


# MENU


menu = {
    "Burger": 4,
    "Pizza": 8,
    "Pasta": 5,
    "Fried Rice": 6,
    "Coffee": 7
}


# MENU DISPLAY FUNCTION


def display_menu():

    print("-" * 36)
    print("              MENU")
    print("-" * 36)

    for item, price in menu.items():
        print(f"{item:<15} ${price}")

    print("-" * 36)


# ADD FOOD ITEM FUNCTION


def add_item():

    item = input("Enter the name of the new food:").title()
    price = int(input("Enter the price:"))

    menu[item] = price

    print(f"{item} has been added to the menu.")


# REMOVE FOOD ITEM FUNCTION


def remove_item():

    item = input("Enter the item you want to remove:").title()

    if item in menu:
        menu.pop(item)
        print(f"{item} has been removed from the menu.")

    else:
        print("The item is not avaiable in the menu.")


# UPDATE THE FOOD PRICE FUNCTION


def update_price():

    item = input("Enter the food item:").title()

    if item in menu:

        new_price = int(input("Enter the new price:"))

        menu[item] = new_price

        print(f"The price of {item} has been updated to ${new_price}.")

    else:
        print("The item is not available in the menu.")


# MENU MANAGEMENT FUNCTION


def manage_menu():

    while True:

        print("\n" +"="*36)
        print(" MENU MANAGEMENT")
        print("="*36)

        print("1. Add Food Item")
        print("2. Remove Food Item")
        print("3. Update Food Item")
        print("4. Display Menu")
        print("5. Back")

        choice = input("Enter your choice:")

        if choice == "1":
            add_item()

        elif choice == "2":
            remove_item()
            
        elif choice == "3":
            update_price()

        elif choice == "4":
            display_menu()

        elif choice == "5":
            break

        else:
            print("Invalid Choice, please try again.")



# ORDER MANAGEMENT FUNCTION


def place_order():

    orders = []
    total = 0

    while True:

        order = input(
            "\nEnter the item from menu (or press 'q' to finish): "
        ).title()

        if order == "Q":
            break

        if order in menu:

            quantity = int(input("Enter quantity: "))

            price = menu[order]
            item_total = price * quantity

            orders.append([order, quantity, item_total])

            total = total + item_total

            print(f"{quantity} x {order} added to your order.")
            print(f"Item total: $ {item_total}")

        else:
            print("The item is not available.")

    return orders, total


# BILL GENERATION FUNCTION


def generate_bill(customer_name, table_number, orders, total):

    print("=" * 36)
    print("            YOUR BILL")
    print("=" * 36)

    print(f"Customer: {customer_name}")
    print(f"Table No: {table_number}")

    print("-" * 36)
    print(f"{'ITEM':<16}{'QTY':<5}{'AMOUNT'}")

    for order in orders:
        print(f"{order[0]:<15} {order[1]:<5}${order[2]}")

    print("-" * 36)
    print(f"{'TOTAL':<27} ${total}")

    print("=" * 36)
    print("    Thank you for dining with us!")
    print("         Have a great day ♡")
    print("=" * 36)


# MAIN MENU FUNCTION

def main_menu():

    while True:

        print("=" * 36) 
        print(" MAIN MENU") 
        print("=" * 36)

        print("1. Customer Order")
        print("2. Manage Menu")
        print("3. Exit")

        choice = input("Enter your choice:")

        if choice == "1":

            customer_name,table_number = get_customer_details()

            display_menu()

            orders,total = place_order()

            generate_bill( customer_name,table_number,orders,total )

        elif choice == "2":

            manage_menu()

        elif choice == "3":

            print("Thank You for using the Restaurant Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# ==========================================
#             RUN THE PROGRAM
# ==========================================

main_menu()