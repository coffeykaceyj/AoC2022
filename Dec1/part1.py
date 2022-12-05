file = open('Dec1/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

currentElfCal = 0
maxElfCal = 0

for line in input:
    if len(line):
        currentElfCal += int(line)
    else:
        if currentElfCal > maxElfCal:
            maxElfCal = currentElfCal
        currentElfCal = 0
        
print(maxElfCal)