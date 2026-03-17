choice = input("(kg to lbs | lbs to kg): ")
if (choice == "kg to lbs") :
    kg = float(input("Enter kg: "))
    print(f"{kg} kg = {kg * 2.205} lbs")
elif (choice == "lbs to kg"):
    lbs = float(input("Enter lbs: "))
    print(f"{lbs} lbs = {lbs / 2.205} kg")
else:
    print("Invalid choice")