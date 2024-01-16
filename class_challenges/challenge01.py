class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, sensor_range = 10, direction = 180):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, speed, new_direction):
        self.motor_speed = speed
        self.direction = new_direction
        # return speed, new_direction
    
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range 
        # return new_sensor_range 
    

# robot_1 = DriveBot(5, 10, 90)
# print(robot_1.motor_speed)
# print(robot_1.direction)
# print(robot_1.sensor_range)

# robot_1.control_bot(10, 180)
# robot_1.adjust_sensor(20)

# print(robot_1.motor_speed)
# print(robot_1.direction)
# print(robot_1.sensor_range)
        
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

DriveBot.all_disabled = True
DriveBot.latitude = -50.0
DriveBot.longitude = 50.0