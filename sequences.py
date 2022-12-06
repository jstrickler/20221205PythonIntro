ctemps = [-40, 0, 37, 75, 26.9, 100]

for c in ctemps:
    f = ((9 * c) / 5) + 32
    print(f"{c:5.1f}\u00B0 C is {f:5.1f}\u00B0 F")
print()

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

clean_fruits = [f.strip().lower() for f in fruits]
print(f"clean_fruits: {clean_fruits}")

