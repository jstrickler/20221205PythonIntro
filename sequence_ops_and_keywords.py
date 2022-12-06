

cities = ['San Diego', 'Dallas', 'Minneapolis', 'Richmond', 'Las Vegas',
          'Phoenix', 'Durham', 'Tampa', 'Dublin']

for city in 'Durham', 'San Antonio', 'Topeka', 'Tampa':
    print(city, city in cities)
print()

if 'Tuscaloosa' not in cities:
    print("NOT IN")
print()

foo = ['a', 'b', 'c']
bar = ['d', 'e', 'f']
result = foo + bar
print(f"result: {result}")

flags = [0] * 10
print(f"flags: {flags}")
print('-' * 60)
print(f"'Python!' * 10: {'Python!' * 10}")
x = [1, 2, 3]
print(f"x * 5: {x * 5}")

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(min(nums), min(fruits))
print(max(nums), max(fruits))
print(sorted(nums))
print(sorted(fruits))
print()
print(len(nums), len(fruits))

rev_fruits = reversed(fruits)
print(f"rev_fruits: {rev_fruits}")












