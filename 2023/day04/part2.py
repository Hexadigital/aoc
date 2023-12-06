cards = {}

with open('input') as in_file:
    for line in in_file.readlines():
        if len(line.strip()) > 0:
            card_num = int(line.split(": ")[0].split("Card ")[1])
            cards[card_num] = line.strip().split(": ")[1].replace('  ', ' ')

# Process initial batch of cards
new_cards = []
total = len(cards.keys())
for card_num in cards.keys():
    card = cards[card_num]
    card_value = 0
    winning_numbers = card.split(' | ')[0].split(' ')
    card_numbers = card.split(' | ')[1].split(' ')
    for n in card_numbers:
        if n in winning_numbers:
            card_value += 1
    if card_value > 0:
        for i in range(0, card_value):
            print("Card", card_num, "with a score of", card_value, "added a copy of card", card_num + i + 1)
            new_cards.append((card_num + i + 1, cards[card_num + i + 1]))
            total += 1

print(new_cards)
while True:
    if len(new_cards) == 0:
        break
    cards_to_check = new_cards.copy()
    new_cards.clear()
    for card_num, card in cards_to_check:
        card_value = 0
        winning_numbers = card.split(' | ')[0].split(' ')
        card_numbers = card.split(' | ')[1].split(' ')
        for n in card_numbers:
            if n in winning_numbers:
                card_value += 1
        if card_value > 0:
            for i in range(0, card_value):
                print("Dupe", card_num, "with a score of", card_value, "added a copy of card", card_num + i + 1)
                new_cards.append((card_num + i + 1, cards[card_num + i + 1]))
                total += 1

print(total)
