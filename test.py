import time

timer = int(input("Enter countdown: "))
for i in range(timer):
    print(timer - i)
    time.sleep(1)
print("Times up")