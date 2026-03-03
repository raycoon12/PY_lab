import math
from math import sin,radians
from random import uniform
from warnings import catch_warnings

GRAVITY = 9.81
SCALE = 0.9
LENGTH = 80
IMPACT_RADIUS = 2
def get_input():
    while True:
        angle = float(input("kąt: "))
        if not (angle >= 0 and angle <= 90):
            print("Kąt poza zakresem")
        else:
            break
    velocity = float(input("prędkość pocz: "))
    return angle, velocity

def calculate_impact(angle, velocity, offset):
    z = velocity ** 2 * sin(radians(angle) * 2) / GRAVITY + offset
    return z

def print_impact(impact, pos1, pos2):
    scaled_impact = round(SCALE * impact)
    print(scaled_impact)
    ground = ["_"]*LENGTH
    ground[pos1] = "1"
    ground[pos2] = "2"
    try:
        ground[scaled_impact] = "X"
    except IndexError:
        print("Poza skala")
    [print(symbol, end="") for symbol in ground]
    print()

def start_game():
    start1 = uniform(0, LENGTH/2)
    start2 = uniform(LENGTH/2+1, LENGTH)
    return round(start1), round(start2)

def check_hit(pos_impact, pos):
    return abs(pos_impact-pos) <= IMPACT_RADIUS

def main():
    pos1, pos2 = start_game()
    while True:
        angle, velocity = get_input()
        print(angle)
        print(velocity)
        z = calculate_impact(angle, velocity, pos1/SCALE)
        print(z)
        print_impact(z, pos1, pos2)
        print(check_hit(z, pos2/SCALE))

if __name__ == "__main__":
    main()

