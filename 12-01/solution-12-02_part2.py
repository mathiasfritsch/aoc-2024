from arepl_dump import dump 

with open('input_tryout.txt') as f:
    lines = f.readlines()


lista = []
listb = []

for line in lines:
    a, b = line.strip().split('  ')
    lista.append(int(a))
    listb.append(int(b))

occurences = []

for number in lista:
    occurences.append((number, number * listb.count(number)))

sum = 0
for numberset in occurences:
    sum += numberset[1]

dump(sum)

