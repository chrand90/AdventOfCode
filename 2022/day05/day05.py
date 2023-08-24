def parse_input(filename):
    with open(filename) as f:
        data, moves = f.read().split('\n\n')

        moves = [(int(y[1]), int(y[3]), int(y[5])) for y in (x.split() for x in moves.split('\n'))]

        data = [x for x in data.split('\n')]
        no_cols = int((data[-1].split())[-1])

        data.reverse()
        data = [x[1::4] for x in data[1:]]
        cols = [''] * no_cols
        for col in data:
            for i in range(len(col)):
                if col[i] != " ":
                    cols[i] += (col[i])

        return cols, moves


def part1():
    data, moves = parse_input('input.txt')
    for (number, source, target) in moves:
        to_move = data[source - 1][-number:]
        to_move = to_move[::-1]
        data[source - 1] = data[source - 1][:-number]
        data[target - 1] += to_move

    print("".join([x[-1] for x in data]))


def part2():
    data, moves = parse_input('input.txt')
    for (number, source, target) in moves:
        to_move = data[source - 1][-number:]
        data[source - 1] = data[source - 1][:-number]
        data[target - 1] += to_move

    print("".join([x[-1] for x in data]))


if __name__ == '__main__':
    part1()
    part2()
