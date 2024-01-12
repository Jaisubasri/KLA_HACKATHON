import math

def calculate_points(diameter, no_point, angle):
    if angle == 0:
        # For a line, calculate points between (-diameter/2, 0) and (diameter/2, 0)
        delta_x = diameter / (no_point - 1) if no_point > 1 else diameter
        points = [(round(-diameter / 2 + i * delta_x, 4), 0) for i in range(no_point)]
    else:
        # For a circular arc, calculate points on the circumference
        radius = diameter / 2
        delta_theta = angle / max(no_point - 1, 1)
        points = [(round(radius * math.cos(math.radians(i * delta_theta)), 4),
                   round(radius * math.sin(math.radians(i * delta_theta)), 4)) for i in range(no_point)]

    return points

# Example usage
diameter = 300  # diameter of the line
no_point = 30   # number of points
angle = 0       # angle

points = calculate_points(diameter, no_point, angle)

for val in points:
    print(val)

