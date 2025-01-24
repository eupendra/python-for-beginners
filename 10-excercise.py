# Shopping Discount Program
amt = input("Enter total amount: ")

if amt.isdigit():
    amt = float(amt)
    disc = 0

    if amt > 5000:
        disc = 0.2  # 20% discount
    elif amt >= 2000:
        disc = 0.1  # 10% discount

    final = amt - amt * disc

    print("Original Amount", amt)
    print("Discount Applied", disc*100, "%")
    print("Due Today", final)
    print("==========================")
    print("YOU SAVED", amt * disc)
    print("==========================")

else:
    print("Invalid input. Enter a number.")
