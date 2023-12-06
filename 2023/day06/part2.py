lines = []

with open('input') as in_file:
    for line in in_file.readlines():
        while ' ' in line:
            line = line.replace(' ', '')
        lines.append(line)

times = [int(lines[0].split(':')[1])]
distances = [int(lines[1].split(':')[1])]

total_solutions = 0

for race in range(0, len(times)):
    winning_solutions = 0
    for start_time in range(0, times[race] + 1):
        print('Race', race, 'with a start time of', start_time, 'results in', start_time * (times[race] - start_time))
        if (start_time * (times[race] - start_time)) > distances[race]:
            winning_solutions += 1
    if total_solutions == 0:
        total_solutions += winning_solutions
    else:
        total_solutions *= winning_solutions
        

print(total_solutions)
