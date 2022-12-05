file = open('Dec1/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines]

currentElfCal = 0
maxElvesCals = [0, 0, 0]

for line in input:
    if len(line) > 0:
        currentElfCal += int(line)
    else:
        if currentElfCal > maxElvesCals[0]:
            maxElvesCals[0] = currentElfCal
            maxElvesCals.sort()
        currentElfCal = 0
        
print(sum(maxElvesCals))

