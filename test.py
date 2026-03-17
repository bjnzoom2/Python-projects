initAmount = float(input("Enter principal amount: $"))
annualInterest = float(input("Enter annual interest rate: ")) / 100
compoundingFrequency = float(input("Enter compounding frequency: "))
time = float(input("Enter amount of time: "))
finalAmount = 0

finalAmount = initAmount * (1 + annualInterest / compoundingFrequency) ** (compoundingFrequency * time)
print(f"Principal Amount: ${initAmount:.2f}\nAnnual Interest: {annualInterest * 100:.2f}%\nCompounding Frequency: {compoundingFrequency:.2f}\nTime: {time:.2f} years\nFinal Amount: ${finalAmount:.2f}")