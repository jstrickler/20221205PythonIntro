from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for _ in range(2):
            self.cards.append("** JOKER **")


