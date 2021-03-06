# Make a robot called myrobot that starts at
# coordinates 30, 50 heading north (pi/2).
# Have your robot turn clockwise by pi/2, move
# 15 m, and sense. Then have it turn clockwise
# by pi/2 again, move 10 m, and sense again.
#
# Your program should print out the result of
# your two sense measurements.
#
# Don't modify the code below. Please enter
# your code at the bottom.

from math import *
import robot

####   DON'T MODIFY ANYTHING ABOVE HERE! ENTER CODE BELOW ####

myrobot = robot.Robot()
# set noise parameters
myrobot.set_noise(5.0, 0.1, 5.0)
myrobot.set(30, 50, pi / 2)
myrobot = myrobot.move(-pi / 2.0, 15.0)
print myrobot.sense()
myrobot = myrobot.move(-pi / 2.0, 10.0)
print myrobot.sense()

