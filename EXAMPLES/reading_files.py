
FILE_NAME = '../DATA/mary.txt'

mary_in = open(FILE_NAME)  # open file for reading
# read file...
mary_in.close()  # close file (easy to forget to do this!)

with open(FILE_NAME, "r") as mary_in:  # open file for reading
    for raw_line in mary_in:  # iterate over lines in file (line retains \n)
        line = raw_line.rstrip()  # rstrip('') removes whitespace (including \n or \r ) from end of string
        print(line)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()  # read entire file into one string
    print("NORMAL:")
    print(contents)
    print("=" * 20)
    print("RAW:")
    print(repr(contents))  # print string in "raw" mode
print('-' * 60)

with open(FILE_NAME) as mary_in:
    lines_with_nl = mary_in.readlines()  # readlines() reads all lines into an array
    print(lines_with_nl)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    lines_without_nl = mary_in.read().splitlines()  # splitlines() splits string on ' ' into lines
    print(lines_without_nl)

count = 0
party = 'Republican'
output_file_name = f"{party.lower()}s.txt"
with open('../DATA/presidents.txt') as pres_in:
    with open(output_file_name, "w") as pres_out:
        for raw_line in pres_in:
            line = raw_line.rstrip()
            fields = line.split(':')
            if fields[-1] == party:
                pres_out.write(f"{fields[2]} {fields[1]}\n")
                count += 1
print(f"There were {count} presidents from the {party} party")

# get distinct parties
parties = set()
with open('../DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        party = line.split(':')[-1]
        parties.add(party)
print(f"Distinct parties: {parties}")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', "w") as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit.capitalize() + '\n')



