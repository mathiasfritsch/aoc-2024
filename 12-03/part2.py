import re
import os

def read_input():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')
    
    with open(file_path, 'r') as f:
        return ''.join(line.strip() for line in f)

def calculate_sum(input):

    pattern = r'mul\((\b[1-9]\d{0,2}\b),(\b[1-9]\d{0,2}\b)\)'
    matches = re.findall(pattern, input)

    sum = 0

    for i, (num1, num2) in enumerate(matches, 1):
        sum += int(num1) * int(num2)
    return sum

input = read_input()

pattern = r'do\(\)(.*?)don\'t\(\)'

matches = re.findall(pattern, "do()" + input + "don't()")

sum = 0

for i, match in enumerate(matches, 1):

    sum += calculate_sum(match)



