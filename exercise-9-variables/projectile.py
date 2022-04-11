from math import pi, tan, cos
deg = 80
theta = deg * (pi/180)
g = 9.81
v = 44
x = 0.5
yo = 1

y = yo + (x * tan(theta)) - (g * x * x) / (2 * (v * cos(theta)) * (v * cos(theta)))
print(y)