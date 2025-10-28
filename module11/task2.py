
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


class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery_capacity):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity  # in kWh


class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, tank_volume):
        super().__init__(reg_num, max_speed)
        self.tank_volume = tank_volume  # in liters




electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)


electric_car.accelerate(120)
gasoline_car.accelerate(140)


electric_car.drive(3)
gasoline_car.drive(3)


print(f"Electric Car {electric_car.reg_num} has driven {electric_car.distance} km.")
print(f"Gasoline Car {gasoline_car.reg_num} has driven {gasoline_car.distance} km.")
