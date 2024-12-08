from arepl_dump import dump 

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


with open('input_sample.txt') as f:
    lines = f.readlines()

sum = 0

levels = []

for line in lines:
  values = [int(value) for value in line.strip().split(' ')]
  levels.append(values)

for level in levels:
  if safe_level(level):
    print("safe  ", level)
    sum += 1
  else:
    print("unsafe  ", level)

print( sum )

