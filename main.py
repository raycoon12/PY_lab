import math
from math import sin,radians
from random import uniform

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

def print_impact(impact, pos1, pos2):
    scaled_impact = round(SCALE * impact)
    print(scaled_impact)
    ground = ["_"]*LENGTH
    ground[scaled_impact] = "X"
    ground[pos1] = "1"
    ground[pos2] = "2"
    [print(symbol, end="") for symbol in ground]
    print()

def start_game():
    start1 = uniform(0, LENGTH/2)
    start2 = uniform(LENGTH/2+1, LENGTH)
    return round(start1), round(start2)

def main():
    pos1, pos2 = start_game()
    while True:
        angle, velocity = get_input()
        print(angle)
        print(velocity)
        z = calculate_impact(angle, velocity)
        print(z)
        print_impact(z, pos1, pos2)

if __name__ == "__main__":
    main()

