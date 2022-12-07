from anytree import Node, LevelOrderIter
file = open('Dec7/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

def calculate_dir_size(node):
    return sum([n.size for n in LevelOrderIter(node)])

instr = input.pop(0).split(' ')
tree_base = Node(instr[2], size=0, parent=None)
root_dir = tree_base
while len(input):
    instr = input.pop(0).split(' ')
    if instr[0] == '$':
        if instr[1] == 'cd':
            if instr[2] == '..':
                root_dir = root_dir.parent
            else:
                root_dir = Node(instr[2], parent=root_dir, size=0)
    elif instr[0] != 'dir':
        new_leaf = Node(instr[1], parent=root_dir, size=int(instr[0]))

dir_space = []
for node in LevelOrderIter(tree_base):
    if node.size == 0:
        size = calculate_dir_size(node)
        dir_space.append(size)

max_dir_size = 100000

print(sum([x for x in dir_space if x <= max_dir_size]))