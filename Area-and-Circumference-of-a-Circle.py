import math

def circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Input
radius = float(input("Enter radius of the circle: "))

# Calculation and output
area, circumference = circle_properties(radius)
print(f"Area: {area}, Circumference: {circumference}")