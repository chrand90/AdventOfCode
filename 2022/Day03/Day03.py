with open("input.txt") as f:
    data = [x.rstrip() for x in f.readlines()]

elf_group = []
for i in range(int(len(data) / 3)):
    elf_group.append([data[3 * i], data[3 * i + 1], data[3 * i + 2]])

data_split = [[x[0:int(len(x) / 2)], x[int(len(x) / 2):]] for x in data]

incommon_item = [list(set(a) & set(b))[0] for a, b in data_split]

badges = [list(set(a) & set(b) & set(c))[0] for a, b, c in elf_group]


def pik(letter):
    if letter.isupper():
        return ord(letter) - 38
    elif letter.islower():
        return ord(letter) - 96


priorities = [pik(x) for x in incommon_item]

priorities_badges = [pik(x) for x in badges]

#print(sum(priorities))
print(sum(priorities_badges))