schematics = []

with open('input') as in_file:
    for line in in_file.readlines():
        if len(line.strip()) > 0:
            schematics.append(line.strip())

gear_locations = []

for row in range(0, len(schematics)):
    for column in range(0, len(schematics[row])):
        if schematics[row][column] == '*':
            gear_locations.append((row, column))

print(gear_locations)

final_num = 0
gears_to_numbers = {}

for row in range(0, len(schematics)):
    temp_num = ''
    temp_coords = []
    for column in range(0, len(schematics[row]) + 1):
        # If we're not at the end of a row, and we have a number...
        if (column != len(schematics[row])) and schematics[row][column].isnumeric():
            temp_num += schematics[row][column]
            temp_coords.append((row, column))
        # Non-number, or end of row
        else:
            # Only process the number if we have one
            if len(temp_num) > 0:
                to_add = False
                surrounding_coords = []
                for coord in temp_coords:
                    surrounding_coords.append((coord[0], coord[1] + 1))
                    surrounding_coords.append((coord[0], coord[1] - 1))
                    surrounding_coords.append((coord[0] + 1, coord[1]))
                    surrounding_coords.append((coord[0] - 1, coord[1]))
                    surrounding_coords.append((coord[0] + 1, coord[1] + 1))
                    surrounding_coords.append((coord[0] - 1, coord[1] + 1))
                    surrounding_coords.append((coord[0] + 1, coord[1] - 1))
                    surrounding_coords.append((coord[0] - 1, coord[1] - 1))
                # Is there a gear nearby?
                for coord in surrounding_coords:
                    if coord in gear_locations:
                        print(temp_num, 'is near gear', coord)
                        to_add = True
                        if coord not in gears_to_numbers.keys():
                            gears_to_numbers[coord] = []
                        gears_to_numbers[coord].append(temp_num)
                        break
                if not to_add:
                    print(temp_num, 'is not near any gears')
                temp_num = ''
                temp_coords.clear()

print(gears_to_numbers)

for gear in gears_to_numbers.keys():
    if len(gears_to_numbers[gear]) == 2:
        print("Adding", int(gears_to_numbers[gear][0]) * int(gears_to_numbers[gear][1]), "due to gear", gear)
        final_num += int(gears_to_numbers[gear][0]) * int(gears_to_numbers[gear][1])

print(final_num)
