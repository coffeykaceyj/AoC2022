file = open('Dec6/input.txt', 'r')
lines = file.readlines()
input = [line.strip() for line in lines][0]

def is_marker(text):
    for i in text:
        if text.count(i) > 1:
            return False
    return True

for i in range(14, len(input)):
    if is_marker(input[i-14: i]):
        print(i)
        break