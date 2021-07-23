import random

class Wombat:
    def waddle(self):
        print("Waddling!")

class Pigeon:
    def coo(self):
        print("coo coo")

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'

class CardDeck(Wombat, Pigeon):  # object
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

# self:Python::this::Java

    def __init__(self, dealer):
        self.dealer = dealer  # store param as private data
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter PROPERTY
        return self._dealer

    @dealer.setter
    def dealer(self, value):  # setter PROPERTY
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

