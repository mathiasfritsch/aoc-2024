from arepl_dump import dump 

with open('input.txt') as f:
    lines = f.readlines()

lista = []
listb = []

for line in lines:
    a, b = line.strip().split('  ')
    lista.append(int(a))
    listb.append(int(b))


lista.sort()
listb.sort()


list_diff = [abs(lista[i] - listb[i]) for i in range(len(lista))]

sum = 0
for i in list_diff:
    sum += i