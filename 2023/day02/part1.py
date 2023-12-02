with open('input') as in_file:
    games = in_file.readlines()

possible_games = 0

for game in games:
    g = game.split(": ")[1]
    sets = g.split(';')
    valid = True
    for s in sets:
        greens = 0
        reds = 0
        blues = 0
        for c in s.split(', '):
            number, color = c.strip().split(' ')
            if color == 'green':
                greens += int(number)
            elif color == 'red':
                reds += int(number)
            elif color == 'blue':
                blues += int(number)
            else:
                print("Bad color:", color)
        if reds > 12 or greens > 13 or blues > 14:
            valid = False
    if valid:
        possible_games += int(game.split(": ")[0].split("Game ")[1])

print(possible_games)
