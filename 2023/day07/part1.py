def count_cards(hand):
    counts = {}
    for char in hand:
        if char in counts.keys():
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_hand_type(hand):
    counts = count_cards(hand)
    # one kind of card
    if len(counts.keys()) == 1:
        return 7 # five of a kind
    # two different kinds of cards
    elif len(counts.keys()) == 2:
        for card in counts.keys():
            if counts[card] == 4:
                return 6 # four of a kind
            if counts[card] == 3:
                return 5 # full house
    # three different kinds of cards
    elif len(counts.keys()) == 3:
        for card in counts.keys():
            if counts[card] == 3:
                return 4 # three of a kind
        return 3 # two pair
    # four different kinds of cards
    elif len(counts.keys()) == 4:
        return 2 # one pair
    else:
        return 1 # high card
    

hand_strengths = {
    1: 'high card',
    2: 'one pair',
    3: 'two pair',
    4: 'three of a kind',
    5: 'full house',
    6: 'four of a kind',
    7: 'five of a kind'
}

card_strengths = {
    'A':'A',
    'K':'B',
    'Q':'C',
    'J':'D',
    'T':'E',
    '9':'F',
    '8':'G',
    '7':'H',
    '6':'I',
    '5':'J',
    '4':'K',
    '3':'L',
    '2':'M'
}

players = []

with open('input') as in_file:
    for line in in_file.readlines():
        players.append(line.strip())

scored_hands = []

for p in players:
    hand, bet = p.split(" ")
    print(hand, hand_strengths[get_hand_type(hand)])
    valuated_hand = ''
    for c in hand:
        valuated_hand += card_strengths[c]
    scored_hands.append({'hand type': get_hand_type(hand), 'raw hand': hand, 'valuated hand': valuated_hand, 'bet': int(bet)})

ranked_hands = []
# Process by hand strength
for i in range(7, 0, -1):
    current_hands = []
    for hand in scored_hands:
        if hand['hand type'] == i:
            current_hands.append(hand)
    current_hands = sorted(current_hands, key=lambda x: x['valuated hand'])
    ranked_hands += current_hands

print('------')

total_winnings = 0
for i in range(0, len(ranked_hands)):
    total_winnings += (len(ranked_hands) - i) * ranked_hands[i]['bet']
    print(ranked_hands[i]['raw hand'], len(ranked_hands) - i)
print(total_winnings)
