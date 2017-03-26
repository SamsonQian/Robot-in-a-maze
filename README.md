# Robot-in-a-maze
1st project of object-orientated programming with Python. I wanted to experiment with Python and object-orientation. 
This program defines 2 classes, a robot and an underwater robot.
Robot is defined and can move through the maze or go deeper underwater.
Underwater class made for 3-d representation of robot, but visual doesn't show the 3-d orientation
# Robot controls
Robot class:
print(robot_name) to display the description of the robot
robot_name.forward(steps)
robot_name.backward(steps)
robot_name.right(steps)
robot_name.left(steps)
robot.battery   to show the remaining battery for the robot
robot.recharge()  to recharge the robot battery

Underwater class (inherits Robot class):
robot.depth to show depth of robot
robot.dive(steps)

