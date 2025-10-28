import random

class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours


cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_spd = random.randint(100, 200)
    cars.append(Car(reg, max_spd))

while max(car.distance for car in cars) < 10000:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

print(f"{'Reg No':<8} {'Max Speed':<10} {'Current Speed':<14} {'Distance':<10}")
for car in cars:
    print(f"{car.reg_num:<8} {car.max_speed:<10} {car.speed:<14} {car.distance:<10.2f}")
