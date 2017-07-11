import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

boost = False

while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    print(next_checkpoint_dist, file=sys.stderr)
    speed = int(40 + 60 * (abs(next_checkpoint_angle) < 90))
    if next_checkpoint_dist < 1200:
        speed = 60
    if boost == False and next_checkpoint_dist > 60000 and abs(next_checkpoint_angle) < 3:
        speed = "BOOST"
        boost = True
    h = math.hypot(next_checkpoint_x - x, next_checkpoint_y - y)
    next_checkpoint_x -= int((next_checkpoint_x - x) * (h - 600) / h)
    next_checkpoint_y -= int((next_checkpoint_y - y) * (h - 600) / h)
    print(next_checkpoint_x, next_checkpoint_y, speed)
