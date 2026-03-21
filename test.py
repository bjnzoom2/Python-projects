items = {
    "Cola" : 1.00,
    "Popcorn Small" : 1.50,
    "Popcorn Medium" : 2.50,
    "Popcorn Large" : 4.00
}

bought = []

balance = 8.00
running = True

while running:
    choice = input("Buy  |  End\n")
    if (choice == "Buy"):
        item = input("Enter item name: ")
        if (items.get(item) != None):
            bought.append(item)
            if (balance - items[item] >= 0):
                balance -= items[item]
                print(f"You bought {item}")
            else:
                print("Insufficient balance")
            print(f"Balance: ${balance:.2f}")
        else:
            print("Invalid option")
    elif (choice == "End"):
        running = False

print(f"Balance: {balance:.2f}")
for i in items.keys():
    print(f"{bought.count(i)}x {i}")