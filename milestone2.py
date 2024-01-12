import math
import ast 

def is_point_inside_circle(x, y, diameter):
    radius = diameter / 2
    distance = math.sqrt(x**2 + y**2)
    return distance <= radius

def dfs(x, y, height, width, dia, x_llc, y_llc, index, answer):
    if (
        (x, y) in index or 
        (x_llc, y_llc) in answer or 
        not is_point_inside_circle(x_llc, y_llc, dia)
    ):
        return
    
    index.append((x, y))
    answer.append((x_llc, y_llc))

    dfs(x + 1, y, height, width, dia, x_llc + width, y_llc, index, answer)
    dfs(x, y + 1, height, width, dia, x_llc, y_llc + height, index, answer)
    dfs(x - 1, y, height, width, dia, x_llc - width, y_llc, index, answer)
    dfs(x, y - 1, height, width, dia, x_llc, y_llc - height, index, answer)

def calculate_co_ordinates(dia, wid, heigh, die_vector, ref):

    llc0, llc1 = ref
    val0, val1 = die_vector

    while val0 < llc0 and val0+width<llc0:
        val0 += wid

    while val1 < llc1 and val1+heigh<llc1 :
        val1 += heigh

    if(val0==die_vector[0] and val1==die_vector[1]):
        val0=0
        val1=0
    x_llc, y_llc = val0, val1
    index, answer = [], []
    dfs(0, 0, heigh, wid, dia, x_llc, y_llc, index, answer)
    return index, answer

f = open("Milestone2\Input\Testcase1.txt", "r")
input_values = []  # whole input
values = []        # values
spl_word = ':'
for i in range(4):
    input_values.append(f.readline())
    input_values[i] = input_values[i].replace('\n', '')
    res = input_values[i].split(spl_word, 1)
    values.append(res[1])

dia = int(values[0])
height, width = map(int, values[1].split('x'))
die_vector = ast.literal_eval(values[2])
reference = ast.literal_eval(values[3])

result = []
result0, result1 = calculate_co_ordinates(dia, width, height, die_vector, reference)

# Print the result
"""
for die_index, llc in zip(result0, result1):
    print(f"{die_index}:{llc}")
"""

file = open('milestone2_testcase1.txt', 'w')
for die_index, llc in zip(result0, result1):
    file.write(f"{die_index}:{llc}\n")
file.close()
