import math

def print_circum(radius):
    circumference = 2 * math.pi * radius
    print(f"The circumference of a circle with radius {radius} is {circumference:.5f}")

print_circum(3)
print_circum(5)
print_circum(2.5)