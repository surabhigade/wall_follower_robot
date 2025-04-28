# controllers/my_controller_wall_follower/wall_follower.py

from controller import Robot

class WallFollower:
    def __init__(self, robot):
        self.robot = robot
        self.timestep = int(robot.getBasicTimeStep())
        self.max_speed = 6.28
        
        # Initialize motors
        self.left_motor = robot.getMotor('left wheel motor')
        self.right_motor = robot.getMotor('right wheel motor')
        
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))
        
        self.left_motor.setVelocity(0.0)
        self.right_motor.setVelocity(0.0)
        
        # Set up distance sensors
        self.proximity_sensors = []
        for i in range(8):
            sensor_name = f'ps{i}'
            sensor = robot.getDistanceSensor(sensor_name)
            sensor.enable(self.timestep)
            self.proximity_sensors.append(sensor)

    def follow_wall(self):
        while self.robot.step(self.timestep) != -1:
            self._update_motors()

    def _update_motors(self):
        sensor_values = [sensor.getValue() for sensor in self.proximity_sensors]

        left_detected = sensor_values[5] > 80
        corner_detected = sensor_values[6] > 80
        front_detected = sensor_values[7] > 80
        
        left_speed = self.max_speed
        right_speed = self.max_speed
        
        if front_detected:
            print("Obstacle ahead - rotating right.")
            left_speed = self.max_speed
            right_speed = -self.max_speed
        else:
            if left_detected:
                print("Wall on left side - moving forward.")
                left_speed = self.max_speed
                right_speed = self.max_speed
            else:
                print("No wall on the left - steering left.")
                left_speed = self.max_speed / 8
                right_speed = self.max_speed
            if corner_detected:
                print("Too close to corner - adjusting right.")
                left_speed = self.max_speed
                right_speed = self.max_speed / 8
        
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)
