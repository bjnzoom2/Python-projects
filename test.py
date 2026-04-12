class Car: 
    speed = 0
    
    def __init__(self):
        print("Hi")
        
    def accelerate(self, accel):
        self.speed += accel
        
car1 = Car()

for i in range(10):
    car1.accelerate(i)
    print("Speed:", car1.speed)