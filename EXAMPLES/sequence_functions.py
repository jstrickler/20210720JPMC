#!/usr/bin/env python

colors = ["red", "blue", "green", "yellow", "brown", "black"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print("colors: len is {}; min is {}; max is {}".format(len(colors), min(colors), max(colors)))
print("months: len is {}; min is {}; max is {}".format(len(months), min(months), max(months)))
print()

print("sorted:", end=' ')
for m in sorted(colors):   # <1>
    print(m, end=' ')
print()

phrase = ('dog', 'bites', 'man')
rev_phrase = reversed(phrase)
print("rev_phrase:", rev_phrase)
print(" ".join(rev_phrase))  # <2>
print()

#   new_string = sep_str.join(iterable_of_strings)

first_names = "Bill Bill Dennis Steve Larry".split()
last_names = "Gates Joy Richie Jobs Ellison".split()

full_names = zip(first_names, last_names)  # <3>
print("full_names:", full_names)
print()

for first_name, last_name in full_names:
    print("{} {}".format(first_name, last_name))

full_names = zip(first_names, last_names)  # <3>
print("full_names:", list(full_names))

print(first_names)
enum = enumerate(first_names)
print(enum)
for i, name in enum:
    print(i, name)
print()

# range(max)  range(min, max)  range(min, max, step)
for i in range(5):
    print(i)
print()

for i in range(5, 101, 5):
    print(i, end=', ')
print('\n')





