# controllers/my_controller_wall_follower/run.py

from controller import Robot
from wall_follower import WallFollower

def main():
    robot = Robot()
    controller = WallFollower(robot)
    controller.follow_wall()

if __name__ == "__main__":
    main()
