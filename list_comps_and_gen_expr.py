fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#  [EXPR for VAR in ITERABLE]  [EXPR for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

nums = [800,80,1000,32,255,400,5,5000]
n1 = [float(n) * 5 for n in nums if n > 300]
print("n1:", n1, '\n')


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print(last_names, '\n')

ln_gen = (p[1] for p in people)
fruit_gen = (f.upper() for f in fruits)
print(ln_gen, fruit_gen, '\n')
for last_name in ln_gen:
    print(last_name)
print()
for fruit in fruit_gen:
    print(fruit)


