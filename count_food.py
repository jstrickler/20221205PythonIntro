from collections import Counter

with open('DATA/breakfast.txt') as br_in:
    foods = br_in.read().splitlines()

print(f"foods: {foods}")

food_counts = Counter(foods)
food_counts['waffles'] = 2

print(f"food_counts: {food_counts}")

with open('DATA/presidents.txt') as pres_in:
    states = (line.split(':')[6] for line in pres_in)

    state_counts = Counter(states)

print(f"state_counts: {state_counts}")

