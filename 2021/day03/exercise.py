SAMPLE_INPUT = "sample_input.txt"
PART1_INPUT = "input.txt"

def part1():
    with open(SAMPLE_INPUT, "r") as f:
        digits = f.read().splitlines()
        # digits = [tuple(i.split()) for i in digits]

    most_common_threshold = len(digits) / 2
    most_common = ""
    least_common = ""

    for i in range(0, len(digits[0])):
        digit_sum = sum([int(x[i]) for x in digits])
        if digit_sum > most_common_threshold:
            most_common += str(1)
            least_common += str(0)
        else:
            most_common += str(0)
            least_common += str(1)

    print(int(most_common,2))
    print(int(least_common,2))
    print(int(least_common,2)*int(most_common,2))


    print((~int(most_common,2)) & 0b11111)

def part2():
    with open(PART1_INPUT, "r") as f:
        numbers = f.read().splitlines()

    print(int(calculate_co2_rating(numbers),2)*int(calculate_oxygen_rating(numbers),2))
    


def calculate_oxygen_rating(numbers):
    digits_in_number = len(numbers[0])
    for i in range(0, digits_in_number):
        digit = get_most_common(numbers, i)
        numbers = list(filter(lambda c: c[i] == digit, numbers))
        if len(numbers) == 1:
            return numbers[0]

def calculate_co2_rating(numbers):
    digits_in_number = len(numbers[0])
    for i in range(0, digits_in_number):
        digit = get_least_common(numbers, i)
        numbers = list(filter(lambda c: c[i] == digit, numbers))
        if len(numbers) == 1:
            return numbers[0]


def get_most_common(numbers, pos):
    count = count_digit_at_pos(numbers, pos)
    if (count['1'] >= count['0']):
        return '1'
    else:
        return '0'

def get_least_common(numbers, pos):
    count = count_digit_at_pos(numbers, pos)
    if (count['1'] >= count['0']):
        return '0'
    else:
        return '1'

def count_digit_at_pos(numbers, pos):
    count = {'1':0, '0':0}
    for digit in numbers:
        count[digit[pos]] += 1

    return count


if __name__ == '__main__':
    part2()