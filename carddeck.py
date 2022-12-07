import random

class CardDeck:  # inherits from object
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)




    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self._cards) == 0:
            raise ValueError("Deck is empty")
        return self._cards.pop()

    def __len__(self):  # used with len(x)
        return len(self._cards)

    def __str__(self):  # used with str(x)
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}:{self.dealer}/{len(self)}"

    def to_json(self):
        return "some JSON string...."

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self): # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, value): # setter property
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("dealer name must be a string")






