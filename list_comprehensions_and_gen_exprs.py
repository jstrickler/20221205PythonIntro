fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    expr = f.upper()
    f0.append(expr)
print(f"f0: {f0}\n")

#     [expr     for   var in iterable]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f.upper() for f in fruits if len(f) > 7]
print(f"f3: {f3}\n")

f4 = [f for f in fruits if f.startswith('p') if len(f) > 7]
print(f"f4: {f4}\n")

f5 = [f[0].upper() for f in fruits]
print(f"f5: {f5}\n")

f6 = [f[:3].upper() for f in fruits]
print(f"f6: {f6}\n")

f7 = [f[0].upper() + f[1:] for f in fruits]
print(f"f7: {f7}\n")

f8 = [f.title() for f in fruits]
print(f"f8: {f8}\n")

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

last_names = [p[1] for p in people]
print(f"last_names: {last_names}\n")

names = [f"{p[0]} {p[1]}" for p in people if p[-1] > '1969']
print(f"names: {names}\n")

s = "my hovercraft is full of eels"
print(f"s.capitalize(): {s.capitalize()}")
print(f"s.title(): {s.title()}")
print()

f1 = [f.upper() for f in fruits]  # list comprehension
f_gen = (f.upper() for f in fruits)  # generator expression
print(f"f_gen: {f_gen}")
for fruit in f_gen:
    print(fruit, end=', ')
print('\n')
print(f"type(f1): {type(f1)}")
print(f"type(f_gen): {type(f_gen)}")



