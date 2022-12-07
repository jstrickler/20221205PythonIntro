
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print(f"f1: {f1}\n")

nums = [800, 0xDeadBeef, 0b10001, 80, 1000, 32, 255, 400, 5, 5000]
n1 = sorted(nums)
print(f"n1: {n1}\n")

#  result = sorted(iterable_to_sort, key=key_function)

#  key=FUNC
#  def f(item):
#     return comparison_value

#  str.upper(s)
f2 = sorted(fruits, key=str.upper)
print(f"f2: {f2}\n")

def ignore_case(word):
    compare_value = word.upper()
    print(f"Comparing {word} as {compare_value}")
    return compare_value

f3 = sorted(fruits, key=ignore_case)
print(f"f3: {f3}\n")

f4 = sorted(fruits, key=len)
print(f"f4: {f4}\n")

f5 = sorted(fruits, key=len, reverse=True)
print(f"f5: {f5}\n")

def custom_sort(fruit):
    return len(fruit), fruit.lower()  # return tuple X, Y

f6 = sorted(fruits, key=custom_sort)
print(f"f6: {f6}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(p):
    return p[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

def by_last_first(p):
    return p[1:0:-1]  # weirdness!!

for person in sorted(people, key=by_last_first):
    print(person)
print('-' * 60)


n2 = sorted(nums, key=str)
print(f"n2: {n2}\n")

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'LTN': 'London',  # (Luton)
    'LGW': 'London',  # (Gatwick)
    'LHR': 'London',  # (Heathrow)
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

def by_city(kv_pair):
    print("pair:", kv_pair)
    return kv_pair[1], kv_pair[0]   #  value, key

sorted_items = sorted(airports.items(), key=by_city)
print(f"sorted_items: {sorted_items}\n")

# for code, city in sorted_items:
#     print(code, city)
# print('-' * 60)

# sort ANY dictionary by value, then key
def by_value(item):
    return item[1], item[0]

for code, city, in sorted(airports.items(), key=lambda a: (a[1], a[0])):
    print(code, city)

# lambda param: (return-value)
