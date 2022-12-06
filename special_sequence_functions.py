
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


rev_fruits = reversed(fruits)
print(f"rev_fruits: {rev_fruits}")
for fruit in rev_fruits:
    print(fruit, end=' ')
print('\n')

rev_fruits = reversed(fruits)
print(list(rev_fruits))
print(list(rev_fruits))
print('-' * 60)

for i, fruit in enumerate(fruits):
    print(i, fruit)
print('-' * 60)
for i, fruit in enumerate(reversed(fruits)):
    print(i, fruit)
print('-' * 60)
print('-' * 60)

# range(stop)  range(start, stop)  range(start, stop, step)
MAX_TRIES = 3

for _ in range(MAX_TRIES):
    print("Hip! Hip! Hooray!")
print()

for i in range(1, 11):
    print(f"Round {i}")
print()

for i in range(5, 101, 5):
    print(i, end=" ")
print('\n')




