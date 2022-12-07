
# find geometry.py in EXAMPLES/alpha/mathlib
from EXAMPLES.alpha.mathlib import geometry
import sys

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

print(f"geometry.PI: {geometry.PI}\n")

# module search order
# 1. current folder (always)
# 2. FOLDERS in PYTHONPATH
# 3. Python installation folder + '/lib'

for path in sys.path:
    print(path)

