import sys
from jpmc import johnlib   #  jpmc/johnlib.py

print(type(johnlib))

johnlib.spam()
johnlib.toast()
print(johnlib.get_animal())

print(johnlib.ANIMAL)

# module search
# 1. current folder
# 2. folders in PYTHONPATH (if it exists)
# 3. sys.prefix/...   Python installation folder

for path in sys.path:  # list of folders to search for modules/packages
    print(path)
print()
print(sys.prefix)

