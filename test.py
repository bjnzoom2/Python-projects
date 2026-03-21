import random
guessed = False

while not guessed:
    num = random.randint(0, 100)
    if (input("Enter number: ") == str(num)):
        print("Guessed correctly")
        guessed = True
    else:
        print(f"Try again\nNumber was: {num}")