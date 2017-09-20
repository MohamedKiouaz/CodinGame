import sys
import math
import numpy as np

laps = int(input())
checkpointCount = int(input())

checkpointX, checkpointY = [], []
for i in range(checkpointCount):
    x, y = [int(i) for i in input().split()]
    checkpointX += [x]
    checkpointY += [y]

boost1 = boost2 = False

def lemme1(x1, y1, x2, y2, R):
    h = math.hypot(x2 - x1, y2 - y1)
    return int(x1 + (x2 - x1) / h * R), int(y1 + (y2 - y1) / h * R)

while True:
    x1, y1, vx1, vy1, angle1, next_checkpoint_1 = [int(i) for i in input().split()]
    x2, y2, vx2, vy2, angle2, next_checkpoint_2 = [int(i) for i in input().split()]
    ox1, oy1, ovx1, ovy1, oangle1, onext_checkpoint_1 = [int(i) for i in input().split()]
    ox2, oy2, ovx2, ovy2, oangle2, onext_checkpoint_2 = [int(i) for i in input().split()]

    targetx1, targety1 = lemme1(checkpointX[next_checkpoint_1], checkpointY[next_checkpoint_1], (checkpointX[(next_checkpoint_1 + 1) % checkpointCount] + x1) / 2, (checkpointY[(next_checkpoint_1 + 1) % checkpointCount] + y1)/2, 400)
    D1 = math.hypot(x1 - targetx1, y1 - targety1)
    speed1 = 40 + 60 * (D1 > 1)
    if(boost1 == False and D1 > 5000):
        speed = "BOOST"
        boost1 = True
    
    targetx2, targety2 = lemme1(checkpointX[next_checkpoint_2], checkpointY[next_checkpoint_2], (checkpointX[(next_checkpoint_2 + 1) % checkpointCount] + x2) / 2, (checkpointY[(next_checkpoint_2 + 1) % checkpointCount] + y2)/2, 400)
    D2 = math.hypot(x2 - targetx2, y2 - targety2)
    speed2 = 40 + 60 * (D2 > 1)
    if(boost2 == False and D2 > 5000):
        speed = "BOOST"
        boost2 = True
    print(boost1, boost2, file=sys.stderr)
    print(targetx1, targety1, speed1)
    print(targetx2, targety2, speed2)
