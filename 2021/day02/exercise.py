SAMPLE_INPUT = "sample_input.txt"
PART1_INPUT = "input.txt"

def part1():
    with open(PART1_INPUT, "r") as f:
        measurements = f.read().splitlines()
        measurements = [tuple(i.split()) for i in measurements]

    keys = set([i[0] for i in measurements])
    dic = dict.fromkeys(keys, 0)

    for direction, magnitude in measurements:
        dic[direction]+=int(magnitude)

    horizontal = dic['forward']
    depth = dic['down'] - dic['up']

    print("horizontal: "+str(horizontal))
    print("depth: "+str(depth))
    print("total: "+str(depth*horizontal))

def part2():
    with open(PART1_INPUT, "r") as f:
        measurements = f.read().splitlines()
        measurements = [tuple(i.split()) for i in measurements]

    aim = 0
    horizontal = 0
    depth = 0

    for direction, magnitude in measurements:
        if direction == 'forward':
            horizontal += int(magnitude)
            depth += aim*int(magnitude)
        elif direction == 'up':
            aim -= int(magnitude)
        elif direction == 'down':
            aim += int(magnitude)

    print("horizontal: "+str(horizontal))
    print("depth: "+str(depth))
    print("total: "+str(depth*horizontal))

if __name__ == '__main__':
    print("*************")
    print("Part 1 answer:")
    part1()
    print("*************")
    print("*************")
    print("Part 2 answer:")
    part2()
    print("*************")
