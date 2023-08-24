

selection_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

game_points = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0, 
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0, 
    ('C', 'Z'): 3
}

winnning_points = {
    'X': 0,
    'Y': 3,
    'Z': 6
}


selection_points_part_2 = {
    ('A', 'X'): 3,
    ('A', 'Y'): 1,
    ('A', 'Z'): 2,
    ('B', 'X'): 1, 
    ('B', 'Y'): 2,
    ('B', 'Z'): 3,
    ('C', 'X'): 2,
    ('C', 'Y'): 3, 
    ('C', 'Z'): 1
}


with open("input.txt") as f:
    games = [tuple(line.split()) for line in f.readlines()]

sum = 0
sum_part2 = 0

for game in games:
    sum += game_points[game] + selection_points[game[1]]
    sum_part2 += selection_points_part_2[game] + winnning_points[game[1]]
    print(selection_points_part_2[game])
    print(winnning_points[game[1]]) 

print(sum)
print(sum_part2)