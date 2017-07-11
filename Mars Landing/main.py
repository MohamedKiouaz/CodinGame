import sys
import math
import numpy as np

surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    if i > 0:
        if previous_land_y == land_y:
            target_x = (previous_land_x + land_x)/2
            target_y = land_y
            radius = abs(previous_land_x - land_x)/2
    previous_land_y = land_y
    previous_land_x = land_x

print(target_x, file=sys.stderr)

while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    xx = target_x - x
    yy = target_y - y
    tetha = int(np.angle(xx + 1j * yy, True)) + 90
    target_distance = np.linalg.norm(np.array([xx, yy]))

    tetha2 = int(np.angle(h_speed + 1j * v_speed, True)) + 90
    speed = np.linalg.norm(np.array([h_speed, v_speed]))

    angle = np.clip(tetha2 - tetha, -90, 90)
    angle = np.clip(angle, -45, 45)

    tetha2 = np.clip(tetha2, -90, 90)

    print(angle, tetha2, int(target_distance), radius, int(speed), file=sys.stderr)
    
    if yy > 200:
        print(0, 4)
        print("Remontée", file=sys.stderr)
    elif (target_distance < radius and abs(h_speed) > 20):
        print(tetha2, 3 + (speed > 20))
        print("Approche", file=sys.stderr)
    elif target_distance > radius:
        print(int(angle), (3 + (speed > 44)))
        print("Décente", file=sys.stderr)
    else:
        print(0, 3 + (abs(v_speed) > 35))
        print("Atterissage", file=sys.stderr)
