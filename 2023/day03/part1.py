schematics = []

with open('input') as in_file:
    for line in in_file.readlines():
        if len(line.strip()) > 0:
            schematics.append(line.strip())

symbol_locations = []

for row in range(0, len(schematics)):
    for column in range(0, len(schematics[row])):
        if (not schematics[row][column].isnumeric()) and schematics[row][column] != '.':
            symbol_locations.append((row, column))

print(symbol_locations)


final_num = 0

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
                # Is there a symbol nearby?
                for coord in surrounding_coords:
                    if coord in symbol_locations:
                        to_add = True
                if to_add:
                    print("Adding number", temp_num)
                    final_num += int(temp_num)
                else:
                    print("Skipping number", temp_num)
                temp_num = ''
                temp_coords.clear()
                
                

print(final_num)
