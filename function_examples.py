import math

def hello(whom="world"):  # default value for parameter
    print(f"Hello, {whom}")

hello('world')
hello('Mom')
hello('Uncle Fred')
hello()
# print(f"r: {r}")

def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

a = circle_area(5)
print(f"a: {a}")

def square_area(length, width):
    return length * width

a = square_area(3, 10)
print(f"a: {a}")

