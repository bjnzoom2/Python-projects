operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))

if (operator == "+") :
    print(f"{num1} + {num2} = {num1 + num2}")
elif (operator == "-") :
    print(f"{num1} - {num2} = {num1 - num2}")
elif (operator == "*") :
    print(f"{num1} * {num2} = {num1 * num2}")
elif (operator == "/") :
    print(f"{num1} / {num2} = {num1 / num2}")