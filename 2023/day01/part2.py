lines = []

with open('input') as in_file:
    for line in in_file:
        lines.append(line)

total = 0

# Find solution with text numbers included
replacements = {
    'one': 'on1e',
    'two': 'tw2o',
    'three': 'th3ree',
    'four': 'fou4r',
    'five': 'fi5ve',
    'six': 's6ix',
    'seven': 'se7ven',
    'eight': 'ei8ght',
    'nine': 'ni9ne'
}

def item_is_in_string(replacements, s):
    for r in replacements.keys():
        if r in s:
            return True
    return False

for line in lines:
    new_line = ''
    print(line)
    
    if item_is_in_string(replacements, line):
        found_items = []
        earliest_number = ''
        earliest_index = 9999
        for r in replacements.keys():
            if r in line:
                if line.index(r) < earliest_index:
                    earliest_number = r
                    earliest_index = line.index(r)
        line = line.replace(earliest_number, replacements[earliest_number], 1)
        
    if item_is_in_string(replacements, line):
        found_items = []
        latest_number = ''
        latest_index = -1
        for r in replacements.keys():
            if r in line:
                if line.rindex(r) > latest_index:
                    latest_number = r
                    latest_index = line.rindex(r)
        line = line[:latest_index] + replacements[latest_number] + line[latest_index + len(latest_number):]
        
    print(line)
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
    print(int(num))
    total += int(num)

print(total)
