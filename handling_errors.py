
FILE_PATH = "DATA/wombats.txt"
try:
    with open(FILE_PATH) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            print(line)
except FileNotFoundError as err:
    # log the error here ...
    print(err)
except PermissionError as err:
    print(err)  # or handle some other way
except Exception as err:
    print("Whoa!", err)

with open('DATA/breakfast.txt') as breakfast_in:
    all_foods = breakfast_in.read().splitlines()
    print(f"all_foods: {all_foods}")

try:
    print(f"all_foods[75]: {all_foods[75]}")
except IndexError as err:
    print(err)
    #  or log...

nums = [0, 800, 80, 0, 1000, 32, 255, "123", 400, 5, "wombat", 5000]

for num in nums:
    try:
        result = 12345 / num
    except (ZeroDivisionError, TypeError, ValueError) as err:
        print(err, type(err))
    else:  # if no exceptions
        print(f"result: {result}")




print("ALL DONE")

