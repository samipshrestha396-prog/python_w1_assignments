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


class Race:
    def __init__(self, name, total_distance, cars):
        self.name = name
        self.total_distance = total_distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Reg No':<8} {'Max Speed':<10} {'Current Speed':<14} {'Distance':<10}")
        for car in self.cars:
            print(f"{car.reg_num:<8} {car.max_speed:<10} {car.speed:<14} {car.distance:<10.2f}")

    def race_finished(self):
        return any(car.distance >= self.total_distance for car in self.cars)





cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]


grand_derby = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not grand_derby.race_finished():
    grand_derby.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\n--- Hour {hours} ---")
        grand_derby.print_status()


print(f"\n--- Race finished after {hours} hours ---")
grand_derby.print_status()
