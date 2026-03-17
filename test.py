operator = input("Enter an operator (+, -, *, /): ")
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

if (operator == "+") :
    print(f"{num1} + {num2} = {num1 + num2}")
elif (operator == "-") :
    print(f"{num1} - {num2} = {num1 - num2}")
elif (operator == "*") :
    print(f"{num1} * {num2} = {num1 * num2}")
elif (operator == "/") :
    print(f"{num1} / {num2} = {num1 / num2}")