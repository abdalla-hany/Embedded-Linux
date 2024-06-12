#Calculate the Area of a Circle using given radius

import math

radius = float(input("Enter the circle radius: "))

area = math.pi * (radius ** 2)
print(type(area))

print(f"The area of the circle with radius {radius} is {area}")