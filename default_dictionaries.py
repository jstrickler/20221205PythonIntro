from collections import defaultdict
from pprint import pprint

def get_zero():
    return 0

zdict = defaultdict(get_zero)
print(f"zdict: {zdict}")

zdict['spam'] = 37
zdict['ham'] = 9
print(f"zdict: {zdict}")
print(f"zdict['spam']: {zdict['spam']}")
print(f"zdict['ham']: {zdict['ham']}")
print(f"zdict['eggs']: {zdict['eggs']}")
print(f"zdict: {zdict}")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fd = defaultdict(list)
for fruit in fruits:
    # if fruit not in fd:
    #     fd[fruit] = list()
    fd[fruit[0]].append(fruit)

pprint(fd, sort_dicts=False)

