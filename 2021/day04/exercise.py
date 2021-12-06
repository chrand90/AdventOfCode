SAMPLE_INPUT = "sample_input.txt"
PART1_INPUT = "input.txt"

def part1_and_2():
    (bingo_boards, drawn_numbers) = get_input()
    play_bingo(bingo_boards, drawn_numbers)

    
def play_bingo(bingo_boards, numbers_to_draw):
    score_by_winning_order = []
    for number in numbers_to_draw:
        for bingo_board in bingo_boards:
            bingo_board.draw_number(number)
            if bingo_board.has_bingo():
                bingo_board.print_boards()
                score_by_winning_order.append(int(number) * bingo_board.get_score())
                bingo_boards.remove(bingo_board)
                

    print("First winner has score:")
    print(score_by_winning_order[0])
    print("Last winner has score:")
    print(score_by_winning_order[-1])

def get_input():
    with open(PART1_INPUT, "r") as f:
        lines = f.read().splitlines()
        # digits = [tuple(i.split()) for i in digits]
    drawn_numbers = lines[0]
    drawn_numbers = drawn_numbers.split(',')

    bingo_boards = []
    bingo_board = []
    for line in lines[2:]:
        if line == '':
            bingo_boards.append(Bingo_Board(bingo_board))
            bingo_board = []
        else:
            bingo_board.append(line)
    bingo_boards.append(Bingo_Board(bingo_board))

    return (bingo_boards, drawn_numbers)


class Bingo_Board:
    def __init__(self, numbers):
        self.numbers = [x.split() for x in numbers]
        self.marked_numbers = [[0 for col in range(len(self.numbers))] for row in range(len(self.numbers[0]))]

    def draw_number(self, number):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[0])):
                if self.numbers[i][j] == number:
                    self.marked_numbers[i][j] = 1

    def has_bingo(self):
        for row in self.marked_numbers:
            if all(val==1 for val in row):
                return True
        for i in range(len(self.marked_numbers[0])):
            col = [x[i] for x in self.marked_numbers]
            if all(val==1 for val in col):
                return True
        return False

    def get_score(self):
        res = 0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[0])):
                if self.marked_numbers[i][j] == 0:
                    res += int(self.numbers[i][j])
        
        return res


    def print_boards(self):
        for row in self.numbers:
            print(str(row))
        for row in self.marked_numbers:
            print(str(row))
        print()


if __name__ == '__main__':
    part1_and_2()