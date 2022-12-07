
x = 100   # GLOBAL variable

def spam():
    print(f"in spam() x: {x}")
    animal = "wombat"   # LOCAL variable
    print(f"animal: {animal}")

spam()
