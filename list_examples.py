import sys

list1 = list()   # empty list
print(f"type(list1): {type(list1)}")
print(f"len(list1): {len(list1)}")
print(f"list1: {list1}")

list2 = ['spam', 'ham', 'toast']
print(f"list2: {list2}")

list3 = []  # empty list
print(f"list3: {list3}")

cities = ['San Diego', 'Dallas', 'Minneapolis', 'Richmond', 'Las Vegas',
          'Phoenix', 'Durham', 'Tampa', 'Dublin']

print(f"len(cities): {len(cities)}")
print(f"cities[0]: {cities[0]}")
print(f"cities[7]: {cities[7]}")
print(f"cities[8]: {cities[8]}")
print(f"cities[len(cities)-1]: {cities[len(cities)-1]}")
print(f"cities[-1]: {cities[-1]}")

cities.insert(0, 'Chicago')
print(f"cities: {cities}")
cities.insert(4, 'Albany')
print(f"cities: {cities}")
cities.append('San Francisco')
cities.append('Tulsa')
print(f"cities: {cities}")

more_cities = ['Sacramento', 'Laramie', 'Atlanta']
cities.extend(more_cities)
print(f"cities: {cities}")

# LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)

pos = cities.index('Minneapolis')
print(f"pos: {pos}")
del cities[pos]
print(f"cities: {cities}")
cities.remove('Albany')
print(f"cities: {cities}")

city = cities.pop(0)
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(5)
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}")

#   del LIST[pos]   LIST.remove(value)   ref = LIST.pop(pos)   ref = LIST.pop()

foods = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'eggs', 'toast',
         'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']

print(f"foods.count('spam'): {foods.count('spam')}")
print(f"foods.count('eggs'): {foods.count('eggs')}")
print(f"foods.count('waffles'): {foods.count('waffles')}")
print()

print(f"cities: {cities}")
print(f"cities[0:4:1]: {cities[0:4:1]}")

print(f"cities[3:6]: {cities[3:6]}") # items 3,4,5
print(f"cities[:5]: {cities[:5]}")
print(f"cities[8:]: {cities[8:]}")
print(f"cities[-4:]: {cities[-4:]}")

print(f"sys.argv: {sys.argv}")
print(f"sys.argv[1:]: {sys.argv[1:]}")

words = ['foo', 'bar', 'blah', 'wombat', 'spam', 'ham', 'tractor']
print(f"words[:-1]: {words[:-1]}")

bdfl = "Guido van Rossum"
print(f"bdfl[-6:]: {bdfl[-6:]}")
print(f"bdfl[:5]: {bdfl[:5]}")
print(f"bdfl[6:9]: {bdfl[6:9]}")
print()

print(f"cities: {cities}")
print()

# for VAR in ITERABLE:
#    ...
for city in cities:
    print(city)
print()

for letter in bdfl:
    print(letter.upper(), end=',')
print('\n')

# iterables: list str bytes tuple dict set *generator*





















