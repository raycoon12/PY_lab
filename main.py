import math
from math import sin,radians
GRAVITY = 9.81
SCALE = 0.9
LENGTH = 80
def get_input():
    while True:
        angle = float(input("kąt: "))
        if not (angle >= 0 and angle <= 90):
            print("Kąt poza zakresem")
        else:
            break
    velocity = float(input("prędkość pocz: "))
    return angle, velocity

def calculate_impact(angle, velocity):
    z = velocity ** 2 * sin(radians(angle) * 2) / GRAVITY
    return z

def print_impact(impact):
    scaled_impact = round(SCALE * impact)
    print(scaled_impact)
    """for i in range(0, LENGTH):
        if i == scaled_impact:
            print("X", end="")
        else:
            print("_", end="")
    print()"""
    ground = ["_"]*LENGTH
    ground[scaled_impact] = "X"
    for symbol in ground:
        print(symbol, end="")
    print()

def main():
    while True:
        angle, velocity = get_input()
        print(angle)
        print(velocity)
        z = calculate_impact(angle, velocity)
        print(z)
        print_impact(z)

if __name__ == "__main__":
    main()

