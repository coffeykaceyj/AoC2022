file = open('Dec8/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]


forest_heights = []
forest_heights_by_column = []
scenic_scores = []

def count_trees_seen(current_tree, trees):
    tree_count = 0
    for tree in trees:
        if tree < current_tree:
            tree_count +=1
        if tree >= current_tree:
            tree_count += 1
            break

    return tree_count

def row_scenic_score(forest, row_index, column_index):
    tree = forest[row_index][column_index]
    left_side = forest[row_index][:column_index]
    left_side.reverse()
    right_side = forest[row_index][column_index + 1:]
    
    return count_trees_seen(tree, left_side) * count_trees_seen(tree, right_side)

def tree_scenic_score(row_index, column_index):
    if row_index == 0 or column_index == 0:
        return 0
    if row_index == len(forest_heights) - 1 or column_index == len(forest_heights[0]) - 1:
        return 0
    
    return row_scenic_score(forest_heights, row_index, column_index) * row_scenic_score(forest_heights_by_column, column_index, row_index)


for line in input:
    row = [int(i) for i in line]
    visibility_row = [False for i in line]
    forest_heights.append(row)

for i in range(len(forest_heights[0])):
    column = []
    for j in range(len(forest_heights)):
        column.append(forest_heights[j][i])
    
    forest_heights_by_column.append(column)


for row_index in range(len(forest_heights)):
    for column_index in range(len(row)):
        tree = forest_heights[row_index][column_index]
        scenic_scores.append(tree_scenic_score(row_index, column_index))

print(max(scenic_scores))