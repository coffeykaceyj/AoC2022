file = open('Dec4/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

def get_section_assignments(line):
    sections = line.split(',')
    return (sections[0].split('-'), sections[1].split('-'))

def is_encompassed(section1, section2):
    if (int(section1[0]) in range(int(section2[0]), int(section2[1])+1) and int(section1[1]) in range(int(section2[0]), int(section2[1])+1)):
        return 1
    elif (int(section2[0]) in range(int(section1[0]), int(section1[1])+1) and int(section2[1]) in range(int(section1[0]), int(section1[1])+1)):
        return 1
    return 0
    
total = 0
for line in lines:
    (section1, section2) = get_section_assignments(line)
    total += is_encompassed(section1, section2)
    
print(total)