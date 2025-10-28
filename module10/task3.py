class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom or target_floor > self.top:
            print("Invalid floor!")
            return
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom = bottom_floor
        self.top = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Running elevator {elevator_number}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number!")

    def fire_alarm(self):
        print("FIRE ALARM! Moving all elevators to bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i}:")
            elevator.go_to_floor(self.bottom)




my_building = Building(0, 10, 3)

my_building.run_elevator(0, 5)
my_building.run_elevator(1, 7)
my_building.run_elevator(2, 3)


my_building.fire_alarm()
