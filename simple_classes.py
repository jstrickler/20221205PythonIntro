
# object =        Class()
# AKA instance
cities = list()   #   list cities = new list();
dogs = list()
dogs.append("Nellie")
wombats = list()

name = "Billy Strings"    #  str name = new str("Billy...")

print(f"type(cities): {type(cities)}")
print(f"type(name): {type(name)}")

class Dog:
    def bark(self):
        print("woof! woof!")

d = Dog()
d.bark()



