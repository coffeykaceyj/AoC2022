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
        new_node = Node(instr[1], parent=root_dir, size=int(instr[0]))

space_used = 0
for node in LevelOrderIter(tree_base):
    space_used += node.size


free_space_required = 30000000
total_space = 70000000
space_to_delete = free_space_required - (total_space - space_used)

dir_space = []
for node in LevelOrderIter(tree_base):
    if node.size == 0:
        size = calculate_dir_size(node)
        dir_space.append(size)

print(min([x for x in dir_space if x >= space_to_delete]))