file = open('Dec8/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]


forest_heights = []
forest_heights_by_column = []
visible_count = 0


def is_visible_in_row(forest, row_index, column_index):
    tree = forest[row_index][column_index]
    left_side = forest[row_index][:column_index]
    right_side = forest[row_index][column_index + 1:]
    if len(right_side) == 0 or len(left_side) == 0:
        return 1
    if tree > max(left_side) or tree > max(right_side):
        return 1

    return 0

def tree_visibility_score(row_index, column_index):
    return is_visible_in_row(forest_heights, row_index, column_index) or is_visible_in_row(forest_heights_by_column, column_index, row_index)


for line in input:
    row = [int(i) for i in line]
    forest_heights.append(row)

for i in range(len(forest_heights[0])):
    column = []
    for j in range(len(forest_heights)):
        column.append(forest_heights[j][i])
    
    forest_heights_by_column.append(column)

for row_index in range(len(forest_heights)):
    for column_index in range(len(row)):
        tree = forest_heights[row_index][column_index]
        visible_count += tree_visibility_score(row_index, column_index)

print(visible_count)
