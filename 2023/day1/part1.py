lines = []

with open('input') as in_file:
    for line in in_file:
        lines.append(line)

total = 0

# Find initial solution
for line in lines:
    new_line = ''
    for i in range(0, len(line)):
        if line[i].isnumeric():
            new_line += line[i]
        else:
            new_line += '|'
    print(new_line)
    while '||' in new_line:
        new_line = new_line.replace('||', '|')
    numbers = new_line.split('|')
    if numbers[0] == '':
        numbers = numbers[1:]
    if numbers[-1] == '':
        numbers = numbers[:-1]
    print(numbers)
    num = numbers[0][0]
    num += numbers[-1][-1]
    total += int(num)

print(total)
