import re
import os

def read_input():
    script_dir = os.path.dirname(__file__)
    with open( os.path.join(script_dir, "input_sample.txt") , "r") as file:
        lines = file.readlines()
        char_2d_array = [list(line.rstrip('\n')) for line in lines]
    return char_2d_array

def xmas_at_location(y,x):
    xmascount = 0
    if x + len(xmas) <= num_columns + 2  and all(input[y][x + k] == xmas[k] for k in range(len(xmas))):
        xmascount += 1
        print( "Found XMAS horizontal at ", y, x)

    if y + len(xmas) <= num_rows + 2  and all(input[y+ k][x] == xmas[k] for k in range(len(xmas))):
        xmascount += 1
        print( "Found XMAS vertical at ", y, x)

    if x + len(xmas) < num_columns + 3  and y + len(xmas) < num_rows + 1  and  all(input[y+ k][x + k] == xmas[k] for k in range(len(xmas))):
        xmascount += 1
        print( "Found XMAS diagonal at ", y, x)

    return xmascount

input = read_input()

xmas = "XMAS"

num_rows = len(input)
num_columns = len(input[0])

allxmas = 0

for y in range(num_rows):
    for x in range(num_columns):
        allxmas = allxmas + xmas_at_location(y,x)

print(allxmas)



