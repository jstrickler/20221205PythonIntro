
import sys   # Import the sys module

print(sys.argv) # Print all parameters, including script itself
script_name = sys.argv[0]
print(f"script_name: {script_name}")

name = sys.argv[1]  # Get the first actual parameter
print("name is", name)


# value = int(sys.argv[1])
