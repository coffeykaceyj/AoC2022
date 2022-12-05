file = open('Dec3/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def find_matching_item(l_comp_items, r_comp_items):
    for item in l_comp_items:
        if item in r_comp_items:
            return(item)

sum = 0
for line in input:
    midway = int(len(line)/2)
    matching_item = find_matching_item(line[:midway], line[midway:])
    priority = items.index(matching_item) + 1
    sum += priority
    
print(sum)
    

