#from arepl_dump import dump 
import os

def check_difference(arr):
    if len(arr) < 2:
        return True

    isIncreasing = arr[0] < arr[1]
    for i in range(1, len(arr)):
        if (isIncreasing and arr[i] < arr[i-1]) or (not isIncreasing and arr[i] > arr[i-1]):
          return False

        diff = abs(arr[i] - arr[i-1])
        if diff < 1 or diff > 3:
          return False

    return True

def safe_level(level):
 return check_difference(level)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')

with open(file_path) as f:
    lines = f.readlines()

sum = 0


levels = []

for line in lines:
  values = [int(value) for value in line.strip().split(' ')]
  levels.append(values)

save = []
reportIndex = 0

for level in levels:
  reportIndex += 1
  if safe_level(level):
    #print("safe at first level", level)
    save.append(reportIndex)
    sum += 1
  else:
    #print("unsafe  at first level", level)
    for i in range(0, len(level)):
      levelToCheck = level[:i] + level[i+1:]

      if safe_level(levelToCheck):
        #print("safe at second level", levelToCheck)
        save.append(reportIndex)
        sum += 1
        break
#print(save)
print( sum )





