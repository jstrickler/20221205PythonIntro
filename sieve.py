
LIMIT = 50

is_prime = [True] * LIMIT

for num in range(2, LIMIT):
    if is_prime[num]:
        print(num, end=",")
        for multiple in range(num, LIMIT, num):
            print(f"Marking {multiple} as non-prime")
            is_prime[multiple] = False

