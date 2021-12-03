from random import shuffle


SUITS = {
    0: 'Diamonds',
    1: 'Hearts',
    2: 'Clubs',
    3: 'Spades'
}

POWERS = {
    2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
    11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'
}


class Card(object):
    def __init__(self, suit, power):
        self.suit = suit
        self.power = power

    def __repr__(self) -> str:
        return '{0:>5} of {1:<8}'.format(POWERS[self.power], SUITS[self.suit])

    def to_row(self):
        return '|{}|'.format(self.__repr__())


def create_deck():
    deck = []
    for suit in range(4):
        for power in range(2, 15):
            deck.append(Card(suit, power))
    return deck


def print_deck(deck):
    print('<{0:-^17}>'.format(''))
    for card in deck:
        print(card.to_row())
    print('<{0:-^17}>'.format(''))


deck = create_deck()
shuffle(deck)

hand = (deck.pop() for _ in range(2))
table = [deck.pop() for _ in range(5)]

print_deck(hand)
print_deck(table)