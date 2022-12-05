file = open('Dec3/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def find_matching_item(rucksack1, rucksack2, rucksack3):
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            return(item)

sum = 0
rucksack1_index = 0
for rucksack1 in input[::3]:
    index = input.index(rucksack1)
    rucksack2 = input[index + 1]
    rucksack3 = input[index + 2]
    matching_item = find_matching_item(rucksack1, rucksack2, rucksack3)
    priority = items.index(matching_item) + 1
    sum += priority
    
print(sum)
    

