import math
from math import sin,radians
GRAVITY = 9.81
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

def main():
    angle, velocity = get_input()
    print(angle)
    print(velocity)
    z = calculate_impact(angle, velocity)
    print(z)

if __name__ == "__main__":
    main()

