#!/usr/bin/env python3

import math

def calculate_area(radius):
    # Mistake 1: The variable "radius" is misspelled as "radus"
    area = math.pi * radius**2
    return area

def main():
    radius = input("Enter the radius of the circle: ")
    radius = float(radius)
    area = calculate_area(radius)
    # Mistake 2: The print statement is missing a closing parenthesis
    print("The area of the circle is", area

if __name__ == "__main__":
    main()
