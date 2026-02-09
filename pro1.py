class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print("Speed increased to:", self.speed)

    def brake(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print("Speed reduced to:", self.speed)

# Object creation
car1 = Car("Maruti", "Swift")

# Method calls
car1.accelerate(40)
car1.brake(15)