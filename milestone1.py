import math
import numpy as np
import sympy as sp
#read the file
def find_line_equation(m, diameter):

    c = diameter / 2    
    return f"y = {m}x + {c}"

def calculate_points(dia,no_point,angle):
    point=[]
    if angle == 0:
        delta_x = dia / (no_point - 1) if no_point > 1 else dia
        point = [(round(-dia / 2 + i * delta_x, 4), 0) for i in range(no_point)]
    else:
        x =  (dia/2) * math.cos(math.radians(angle))
        y =  (dia/2)* math.sin(math.radians(angle))
        x2=x
        y2=y
        x1=-x
        y1=-y
        n=no_point
        delta_x = (x2 - x1) / (n - 1) if n > 1 else x2 - x1
        delta_y = (y2 - y1) / (n - 1) if n > 1 else y2 - y1
        
        point = [(x1 + i * delta_x, y1 + i * delta_y) for i in range(n)]
        
    return point


f = open("Milestone1\Input\Testcase4.txt", "r")
input=[]        # whole input
values=[]       #values
spl_word=':'
for i in range(3):
    input.append(f.readline())
    input[i]=input[i].replace('\n','')
    res = input[i].split(spl_word, 1)
    values.append(int(res[1]))

points=calculate_points(int(values[0]),int(values[1]),int(values[2]))
print(points)

file = open('milestone1_testcase4.txt','w')
for val in points:
	file.write(str(val)+"\n")
file.close()

