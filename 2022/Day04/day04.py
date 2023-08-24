import re


def check_for_subset(a, b, c, d):
    if a >= c and b <= d:
        return True
    elif c >= a and d <= b:
        return True
    else:
        return False


def check_for_overlap(a, b, c, d):
    if c <= b and d >= a:
        return True
    elif a <= d and b >= c:
        return True
    else:
        return False


with open("input.txt") as f:
    data = [x.rstrip() for x in f.readlines()]


endpoints = []
for x in data:
    pik = re.split(r'[,|\-]', x)
    pik = [int(y) for y in pik]
    endpoints.append(pik)

sum = 0
for x in endpoints:
    if check_for_overlap(x[0], x[1], x[2], x[3]):
        sum = sum + 1

print(sum)
