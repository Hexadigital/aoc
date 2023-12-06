cards = []

with open('input') as in_file:
    for line in in_file.readlines():
        if len(line.strip()) > 0:
            cards.append(line.strip().split(": ")[1].replace('  ', ' '))

total = 0
for card in cards:
    card_value = 0
    winning_numbers = card.split(' | ')[0].split(' ')
    card_numbers = card.split(' | ')[1].split(' ')
    for n in card_numbers:
        if n in winning_numbers:
            if card_value == 0:
                card_value += 1
            else:
                card_value *= 2
    total += card_value

print(total)
