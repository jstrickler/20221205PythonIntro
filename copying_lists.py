from copy import deepcopy

my_data = [
    [1, 2, 3],
    [4, 5, 6],
]

print(f"my_data[0]: {my_data[0]}")
my_data.append([7, 8])
print(f"my_data: {my_data}")

my_data[0].append(3.5)
print(f"my_data: {my_data}")

d2 = my_data  # alias for object
my_data.append([9, 10, 11])
print(f"my_data: {my_data}")
print(f"d2: {d2}")
print(f"d2 is my_data: {d2 is my_data}")
print(f"id(my_data): {id(my_data)}")
print(f"id(d2): {id(d2)}")

a = 5  # create object
b = a  # alias to object
print(f"a is b: {a is b}")
a = 10  # create object
print(f"a: {a}")
print(f"b: {b}")

def spam(x):
    print(f"id(x): {id(x)}")


value = 12
print(f"id(value): {id(value)}")
spam(value)

m = [1, 2, 3]
def ham(thing):
    thing.append("wombat")

ham(m)
print(f"m: {m}")

d3 = list(my_data)  # shallow copy
# d3 = my_data[::]
print(f"d3 is my_data: {d3 is my_data}")
d3.append("vampire")
my_data.append('werewolf')
print(f"my_data: {my_data}")
print(f"d3: {d3}")

my_data[1].append("jellybean")
print()
print(f"my_data: {my_data}")
print(f"d3: {d3}")

d4 = deepcopy(my_data)


a = list()
b = a  # alias
c = list(a)  # shallow copy (new list, but references can still be dereferenced)
d = deepcopy(a) # completely new list

