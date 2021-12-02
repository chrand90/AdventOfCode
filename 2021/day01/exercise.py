SAMPLE_INPUT = "example_input.txt"
PART1_INPUT = "input.txt"

def part1():
    with open(PART1_INPUT, "r") as f:
        measurements = f.read().splitlines()
        measurements = [int(i) for i in measurements]
    
    c = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            c+=1
    print(c)


def part2():
    with open(PART1_INPUT, "r") as f:
        measurements = f.read().splitlines()
        measurements = [int(i) for i in measurements]

    c = 0
    for i in range(3, len(measurements)):
        if sum(measurements[i-3:i]) < sum(measurements[i-2:i+1]):
            c+=1
    print(c)

if __name__ == '__main__':
    part2()