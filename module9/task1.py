# Write a Car class that has the following properties: registration number, maximum speed,
# current speed and travelled distance. Add a class initializer
# that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car


class car:
    def __init__(self,reg_num,max_speed):
        self.reg_num=reg_num
        self.max_speed=max_speed
        self.current_speed=0
        self.distance=0


car1=car("ABC-123","142 km/h")
print("Reg_number: ",car1.reg_num)
print("Max_speed: ",car1.max_speed)
print("Current speed: ",car1.current_speed)
print("Travelled distance: ",car1.distance)
