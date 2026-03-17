unit1 = input("Enter unit1 (°C, °F): ")
tempValue = float(input("Enter temperature: "))
unit2 = input("Enter unit2 (°C, °F): ")
if (unit1 == "°C" and unit2 == "°F") :
    print(f"{tempValue}°C = {tempValue * 9.0/5.0 + 32}°F")
elif (unit1 == "°F" and unit2 == "°C") :
    print(f"{tempValue}°F = {(tempValue - 32) * 5.0/9.0}°C")
else:
    print("Invalid conversion")