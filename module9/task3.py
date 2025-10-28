 # Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.


class car:
     def __init__(self, reg_num, max_speed, ):
         self.reg_num = reg_num
         self.max_speed = max_speed
         self.current_speed = 60
         self.distance = 2000

     def acc(self, change):
         self.current_speed += change

         if self.current_speed > self.max_speed:
             self.current_speed = self.max_speed

         elif self.current_speed < 0:
             self.current_speed = 0

     def drive(self, numberof_hours):
         self.distance += self.current_speed * numberof_hours


a = car("ABC-123", 142)
 # a.acc(30)
 # a.acc(70)
 # a.acc(50)

 # print("current speed of the car: ", a.current_speed)
 # a.acc(-200)
 # print("Final speed of the car: ", a.current_speed)

a.drive(1.5)
print(a.distance)