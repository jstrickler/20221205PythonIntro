import json
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Noah")  # CardDeck.__init__(self, "Noah")
print(f"d1: {d1}")
print(f"type(d1): {type(d1)}")
d2 = CardDeck("Ephraim")
d3 = CardDeck("Beatrice")

#  print(d1.get_dealer())  getter method  (AKA accessor)

print(f"d1.dealer: {d1.dealer}")
print(f"d2.dealer: {d2.dealer}")

d2.dealer = "Joshua"  # CardDeck.dealer(d2, "Joshua")
print(f"d2.dealer: {d2.dealer}")

try:
    d2.dealer = 5.9
except TypeError as err:
    print(err)
else:
    print(f"d2.dealer: {d2.dealer}")
print(f"d2.dealer: {d2.dealer}")

print(f"d1.cards: {d1.cards}")

d1.shuffle()

print(f"d1.cards: {d1.cards}")
print()

for _ in range(5):
    card = d1.draw()
    print(f"card: {card}")
print()

print(f"len(d1): {len(d1)}")

print(f"d1: {d1}")
print('-' * 60)
print(d1.__dict__)

serialized = json.dumps(d1.__dict__)
print(f"serialized: {serialized}")
print('-' * 60)
j1 = JokerDeck("Jimmy")
j1.shuffle()
print(f"j1.dealer: {j1.dealer}")
print(f"j1.cards: {j1.cards}")
