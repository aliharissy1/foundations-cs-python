cart = []
total = 0
coupon_total = 0

def newOrder():
    while True:
        try:
            print("Enter:")
            print("1. to add an item")
            print("2. to check total")
            print("3. to add a coupon")
            print("4. to checkout")

            choice = int(input())

            if choice == 1:
                addItem()
            elif choice == 2:
                checkTotal()
            elif choice == 3:
                addCoupon()
            elif choice == 4:
                checkout()
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input. Please enter a valid option.")

def addItem():
    try:
        adding_items = input("Enter the item: ")
        items = [["tomato", 1], ["potato", 2], ["chocolate", 3], ["soap", 0.5]]

        for item in items:
            if adding_items.lower() == item[0].lower():
                cart.append(item)
                print(f"{item[0]} added to the cart.")
                return

        print(f"Sorry, we don't have {adding_items} in our shop.")
    except ValueError:
        print("Invalid input. Please enter a valid item.")

def checkTotal():
    try:
        if not cart:
            print("The cart is empty.")
        else:
            total_price = 0
            print("Items in the cart:")
            for item in cart:
                item_name, item_price = item[0], item[1]
                total_price += item_price
                print(f"{item_name}: ${item_price}")
            print(f"Total bill of all items: ${total_price}")
    except ValueError:
        print("An error occurred while checking the total.")

def addCoupon():
    try:
        global coupon_total
        coupon_value = float(input("Enter the coupon value: "))
        coupon_total += coupon_value
        print(f"Coupon value ${coupon_value} applied to the total.")
    except ValueError:
        print("Invalid value. Please enter a valid coupon value.")

def checkout():
    try:
        global coupon_total
        print("Items bought and their quantities:")
        for item in cart:
            print(f"{item[0]}: {item[1]}")

        total = 0
        for item in cart:
            total += item[1]

        print("Total of the order (without coupons):", total)

        print("Total of the coupons:", coupon_total)

        total_to_pay = total - coupon_total
        print("Total to pay (total of order - total of coupons):", total_to_pay)

        cart.clear()
        coupon_total = 0

        print("Returning to the main menu.")
    except ValueError:
        print("An error occurred during the checkout process.")

def mainMenu():
    while True:
        try:
            print("Enter:")
            print("1. to start a new order")
            print("2. to close the program")

            choice = int(input())

            if choice == 1:
                print("Starting a new order...")
                newOrder()
            elif choice == 2:
                print("Bye bye")
                break
            else:
                print("Invalid input. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid option.")

mainMenu()

