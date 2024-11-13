import math

def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

radius_30 = calculate_volume_of_sphere(30)
radius_40 = calculate_volume_of_sphere(40)
print(f"Volume of sphere with radius 30: {radius_30}")
print(f"Volume of sphere with radius 40: {radius_40}")
