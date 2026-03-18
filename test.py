groceries = []
prices = []
total = 0
registeredGroceries = ["apple", "banana", "grapes", "orange"]
registeredPrices = [2, 3, 6, 4]

running = True

while running: 
    choice = input("Buy  |  Pay\n")
    if (choice == "Pay"):
        running = False
    elif (choice == "Buy"):
        grocery = input("Enter grocery: ")
        y = 0
        found = False
        for x in registeredGroceries:
            found = False
            if (grocery.lower() == x):
                prices.append(registeredPrices[registeredGroceries.index(grocery.lower())])
                found = True
                break
            else:
                continue
                
        if (not found):
            y = float(input("Item not recognised, Enter price: "))
            prices.append(y)

        groceries.append(grocery)
        print(f"{grocery} has been added to cart")
        

for g in groceries:
    p = prices[groceries.index(g)]
    print(f"{g}: ${p:.2f}")
    total += p

print(f"Total Price: ${total:.2f}")