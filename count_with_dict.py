from pprint import pprint

parties = {}
with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        party = fields[-1]
        if party not in parties:
            parties[party] = 0
        parties[party] = parties[party] + 1   # parties[party] += 1
pprint(parties)
print()


food_counts = {}
with open('DATA/breakfast.txt') as food_in:
    for raw_line in food_in:
        food = raw_line.rstrip()
        if food in food_counts:
            food_counts[food] += 1
        else:
            food_counts[food] = 1
pprint(food_counts)






