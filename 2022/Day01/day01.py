from itertools import groupby

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

data = [list(g) for k, g in groupby(lines, key=bool) if k]

data = [[int(element) for element in x] for x in data]
summed = [sum(x) for x in data]
summed.sort()

print(summed[-1])
print(sum(summed[-3:]))
