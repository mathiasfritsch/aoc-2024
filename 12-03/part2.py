import re
import os

def read_input():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')
    with open(file  = file_path) as f:
        return f.read()

input = "_a_12_a_84_a_567_b_98_a_1234_b_88888_b_777_a_666_a_111_b_444_a_333_b_1999_b_23333_a_"

#input = read_input()

#pattern = r'_a_(.*?)pattern = r'_a_(.*?)_b_''

# split the input string by the pattern
pattern = r'_a_(.*?)_b_'

# Find all matches
matches = re.findall(pattern, input)





