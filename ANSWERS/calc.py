import re

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return 0
    return x/y

rx_math_expr = r"\s*(\d*(?:\.\d+)?)\s*([-+/*])\s*(\d*(?:\.\d+)?)\s*"

while True:
    expr = input("Enter a math expression: ")

    if expr.lower() == 'q':
        break

    m = re.match(rx_math_expr, expr)
    if m:
        v1 = m.group(1)
        op = m.group(2)
        v2 = m.group(3)
    else:
        print("invalid expression")
        continue

    try:
        v1 = float(v1)
        v2 = float(v2)
    except ValueError as err:
        print(err)
        continue

    if op == '+':
        result = add(v1, v2)
    elif op == '-':
        result = sub(v1, v2)
    elif op == '*':
        result = mul(v1, v2)
    elif op == '/':
        result = div(v1, v2)
    else:
        print("Bad operator!")
        continue

    print("{:.3f}".format(result))
