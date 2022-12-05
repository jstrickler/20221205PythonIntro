
# int float

i1 = 1000
i2 = 0b1000
i3 = 0x1000
i4 = 0o1000

print(i1, i2, i3, i4)
print()

f1 = 123.456
f2 = 123.
f3 = .3903902
f4 = 1.3985e22  # 1.3985 * (10 ** 22)


a = 23
b = 7
print(a + b, a - b, a * b)
print(a / b, a // b, a % b)
print(a ** b, b ** a)

x = (a * b) + (a - b)
#  P E (MD) (AS)

m = 10
m += 5  #  m = m + 5
m *= 4  #  m = m * 4
m /= 3
print(f"m: {m}")

m += 1  # increment m by 1

# m++ is not implemented
print()

a = "123"
b = 456
print(f"a + str(b): {a + str(b)}")
print(f"int(a) + b: {int(a) + b}")











