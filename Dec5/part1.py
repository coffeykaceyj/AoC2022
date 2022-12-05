file = open('Dec5/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

STACKS = [
        ['Z', 'P', 'B', 'Q', 'M', 'D', 'N'],
        ['V', 'H', 'D', 'M', 'Q', 'Z', 'L', 'C'],
        ['G', 'Z', 'F', 'V', 'D', 'R', 'H', 'Q'],
        ['N', 'F', 'D', 'G', 'H'],
        ['Q', 'F', 'N'],
        ['T', 'B', 'F', 'Z', 'V', 'Q', 'D'],
        ['H', 'S', 'V', 'D', 'Z', 'T', 'M', 'Q'],
        ['Q', 'N', 'P', 'F', 'G', 'M'],
        ['M', 'R', 'W', 'B']
    ]

def move_items(directions):
    move_size = directions[0]
    from_stack = STACKS[directions[1]]
    to_stack = STACKS[directions[2]]
    
    items = from_stack[:move_size]
    items.reverse()
    from_stack = from_stack[move_size:]
    to_stack = [*items, *to_stack]
    return (from_stack, to_stack)

for line in input:
    directions = line.split(' from ')
    directions[0] = directions[0].split('move ')
    directions[1] = directions[1].split(' to ')
    directions = [int(directions[0][1]), int(directions[1][0])-1, int(directions[1][1])-1]
    (from_stack, to_stack) = move_items(directions)
    STACKS[directions[1]] = from_stack
    STACKS[directions[2]] = to_stack
    
for stack in STACKS:
    print(stack[0])