file = open('Dec2/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

WINNING_COMBOS = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
DRAW_COMBOS = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
CHOICE_SCORES = {'X': 1, 'Y': 2, 'Z': 3}


def calculate_round_score(opponent, mine):
    choice_score = CHOICE_SCORES.get(mine)
    result_score = 0
    if [opponent, mine] in WINNING_COMBOS:
        result_score = 6
    elif [opponent, mine] in DRAW_COMBOS:
        result_score = 3
        
    return result_score + choice_score

my_score = 0
for line in lines:
    my_score += calculate_round_score(line[0], line[2])
    
print(my_score)