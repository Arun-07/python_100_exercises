# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:
'''
UP 5
DOWN 3
LEFT 3
RIGHT 2
'''
# The numbers after the direction are steps. Please write a program to compute 
# the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer. 
# Example: If the following tuples are given as input to the program:
'''
UP 5
DOWN 3
LEFT 3
RIGHT 2
'''
# Then, the output of the program should be: 2

import math

up_down, left_right = 0, 0

while True:
    user_input = input().split(' ')
    if not user_input[0]:
        break
    else:
        if user_input[0].lower() == 'up':
            up_down -= int(user_input[1])
            print(up_down)
        elif user_input[0].lower() == 'down':
            up_down += int(user_input[1])
            print(up_down)
        elif user_input[0].lower() == 'left':
            left_right -= int(user_input[1])
            print(left_right)
        elif user_input[0].lower() == 'right':
            left_right += int(user_input[1])
            print(left_right)

total_distance = round(math.sqrt(up_down**2 + left_right**2))
print(total_distance)

