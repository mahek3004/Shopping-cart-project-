print("====== Welcome to Mini Shopping Cart ======")

c = {}  # cart dictionary
t = 0   # total amount

def show_menu():
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        name = input("Enter item name: ").capitalize()
        price = int(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        
        if name in c:
            c[name][1] += qty
        else:
            c[name] = [price, qty]

        print(f"{name} added!")

    elif choice == 2:
        name = input("Enter item to remove: ").capitalize()
        if name in c:
            del c[name]
            print(f"{name} removed!")
        else:
            print("Item not found!")

    elif choice == 3:
        if not c:
            print("Cart is empty!")
        else:
            print("\n--- Your Cart ---")
            t = 0
            for i, (name, data) in enumerate(c.items(), 1):
                price, qty = data
                amount = price * qty
                t += amount
                print(f"{i}. {name} | ₹{price} x {qty} = ₹{amount}")

            print("-----------------")
            print(f"Total = ₹{t}")

    elif choice == 4:
        if not c:
            print("Cart is empty!")
            continue

        print("\n=== FINAL BILL ===")
        t = 0
        for name, data in c.items():
            price, qty = data
            amount = price * qty
            t += amount
            print(f"{name} | ₹{price} x {qty} = ₹{amount}")

        # Reward points logic
        rewards = t // 10  # For every ₹10, 1 point

        # Discount logic
        discount = 0
        if t >= 1000:
            discount = t * 0.10
            print("10% discount applied!")

        final_amt = t - discount

        print("--------------")
        print(f"Total Bill = ₹{t}")
        print(f"Discount = ₹{discount:.2f}")
        print(f"Final Amount = ₹{final_amt:.2f}")
        print(f"You earned {rewards} reward points!")
        print("Thank you for shopping!")
        break

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice!")
