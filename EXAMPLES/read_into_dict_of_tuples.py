#!/usr/bin/env python
from pprint import pprint

knight_info = {}  # <1>

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = title, color, quest, comment  # <2>
        # D[KEY] = VALUE
pprint(knight_info)
print()

#    KEY, VALUE   in  DICT.items()
for name, info in knight_info.items():
    print(info[0], name)

print()
print(knight_info['Robin'])
print(knight_info['Robin'][2])
