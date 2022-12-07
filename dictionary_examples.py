
d1 = dict()   # empty dictionary
d2 =  {'NC': 'Raleigh', 'CA': 'Sacramento', 'NH': 'Concord'}
d2['FL']  = 'Tallahassee'
d2['MD']  = 'Annapolis'
print(f"d2: {d2}")

print(f"d2['CA']: {d2['CA']}\n")

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

print(f"airports.keys(): {airports.keys()}\n")
print(f"airports.values(): {airports.values()}\n")

print(f"airports['YCC']: {airports['YCC']}")
#print(f"airports['DFW']: {airports['DFW']}")

print(f"airports.get('RDU'): {airports.get('RDU')}")
print(f"airports.get('DFW'): {airports.get('DFW')}")
print(f"airports.get('DFW', 'N/A'): {airports.get('DFW', 'N/A')}")
print()
print(f"airports.items(): {airports.items()}\n")

for code, city in airports.items():
    print(code, city)
print()

for code, city in sorted(airports.items()):
    print(code, city)
print()














