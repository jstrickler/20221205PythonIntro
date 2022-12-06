import pandas as pd

fields = 'term last_name first_name dob dod bplace bstate termstart termend party'.split()

df = pd.read_table('DATA/presidents.txt', names=fields, delimiter=":")

print(df.party.value_counts())
print()
print(df.bstate.value_counts())
