import re
import os

#input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)"

# read the input file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')
# get input from file
with open(file  = file_path) as f:
 input = f.read()



import re

pattern = r'mul\((\b[1-9]\d{0,2}\b),(\b[1-9]\d{0,2}\b)\)'

matches = re.findall(pattern, input)

sum = 0

for i, (num1, num2) in enumerate(matches, 1):
    sum += int(num1) * int(num2)

print(sum)




