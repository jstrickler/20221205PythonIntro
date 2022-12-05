s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """
select *
from customers
where state = 'NV'
order by sales desc
"""

print("Hello")

empty = ""   #  ''  """"""  ''''''
data = []  # empty list
stuff = ()  # empty tuple
info = {}  # empty dictionary

actor = "Chris Hemsworth"
print(type(actor))
print(len(actor))

print(f"actor.upper(): {actor.upper()}")
a1 = actor.upper()
print(f"a1: {a1}")

print(f"actor.count('h'): {actor.count('h')}")
print(f"actor.count('H'): {actor.count('H')}")
print(f"actor.lower().count('h'): {actor.lower().count('h')}")

print(f"actor.startswith('Chris'): {actor.startswith('Chris')}")
print(f"actor.startswith('Liam'): {actor.startswith('Liam')}")

print(f"'em' in actor: {'em' in actor}")

print(f"actor.find('Chris'): {actor.find('Chris')}")
print(f"actor.find('or'): {actor.find('or')}")
print(f"actor.find('Liam'): {actor.find('Liam')}")

s = "      My hovercraft is full of eels      "
print(f"s + '|': {s + '|'}")
print(f"s.lstrip() + '|': {s.lstrip() + '|'}")
print(f"s.rstrip() + '|': {s.rstrip() + '|'}")
print(f"s.strip() + '|': {s.strip() + '|'}")
print()

raw_amount = "$$$$.$12,500"
amount = raw_amount.replace(',', '').lstrip('$.')
print(f"amount: {amount}")

date = "Jun 5 2021"
date_parts = date.split()
print(f"date_parts: {date_parts}")

record = 'Joe:Blow:St. Cloud:MN'
fields = record.split(':')
print(f"fields: {fields}")







