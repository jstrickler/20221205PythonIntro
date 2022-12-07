with open('DATA/breakfast.txt') as food_in:
    all_foods = food_in.read().splitlines()
    print(f"all_foods: {all_foods}")
print()

unique_foods = set(all_foods)
print(f"unique_foods: {unique_foods}")

annette_countries = ['Spain', 'Finland', 'Guyana', 'New Zealand', 'Japan',
    'Morocco', 'Myanmar', 'Somalia']
mark_countries = ['Japan', 'Japan', 'Japan', 'Guyana', 'France', 'Iceland',
    'Thailand', 'Finland', 'Morocco']

annette = set(annette_countries)
mark = set(mark_countries)
mark.add('Poland')
annette.add('Spain')
annette.add('Montenegro')
mark.add('France')
print()
print("COMMON:", annette & mark)  # intersection
print("NOT COMMON:", annette ^ mark)  # xor
print("ALL:", annette | mark)  # union
print("ONLY Annette:", annette - mark)
print("ONLY Mark:", mark - annette)


