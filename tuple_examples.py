
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(f"person: {person}")
print(f"type(person): {type(person)}")
print(f"len(person): {len(person)}")
print(f"person[0]: {person[0]}")
print(f"person[1]: {person[1]}")
print(f"person[-1]: {person[-1]}")

first_name, last_name, product, dob = person   #  iterable unpacking

# extended iterable unpacking
values = 'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'eta'
a, b, c, d, e, f = values
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)
print()

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

print(f"type(people): {type(people)}")
print(f"type(people[0]): {type(people[0])}")
print(f"type(people[0][0]): {type(people[0][0])}")
print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")
print()

for person in people:
    print(person[0], person[1])
print()

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print()

info = [('NC', 'Raleigh'), ('TX', 'Austin'), ('CA', 'Sacramento')]

for state, capital in info:
    print(f"{capital} is the capital of {state}")
print()











