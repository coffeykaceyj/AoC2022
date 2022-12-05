file = open('Dec2/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

CHOICE_SCORES = {'A': 1, 'B': 2, 'C': 3}
LOSE_CHOICES = {'A': 'C', 'B': 'A', 'C': 'B'}
WIN_CHOICES = {'A':'B', 'B': 'C', 'C': 'A'}
RESULT_SCORES = {'X': 0, 'Y': 3, 'Z': 6}

def determine_choice(opponent, result):
    if result == 'X':
        return LOSE_CHOICES.get(opponent)
    elif result == 'Z':
        return WIN_CHOICES.get(opponent)
    else:
        return opponent
        

def calculate_round_score(opponent, result):
    mine = determine_choice(opponent, result)
    choice_score = CHOICE_SCORES.get(mine)
    result_score = RESULT_SCORES.get(result)
        
    return result_score + choice_score

my_score = 0
for line in lines:
    
    my_score += calculate_round_score(line[0], line[2])
    
print(my_score)