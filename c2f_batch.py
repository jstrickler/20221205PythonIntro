import sys

celsius_value = float(sys.argv[1])
fahrenheit_value = (( 9 * celsius_value) / 5) + 32

print(f"{celsius_value}\u00B0 C is {fahrenheit_value}\u00B0 F")
