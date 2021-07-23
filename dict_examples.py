#  my %states;     states = {}
#  $states{NC} = "Raleigh";    states['NC'] = "Raleigh"

d1 = dict()  #  empty dict
d2 = {}      # same

capitals = {'NC': 'Raleigh', 'NY': 'Albany', 'CA': 'Sacramento'}
print(capitals['NC'])
print(capitals)
capitals['TX'] = 'Austin'
capitals['SD'] = 'Pierre'
print(capitals)
capitals['NC'] = 'Durham'
print(capitals)
print("TX" in capitals)
print("VA" in capitals)
print(capitals.items())
print(capitals.keys())
print(capitals.values())
capitals['NY'] = None
print(capitals)
del capitals['NY']
print(capitals)

for i, (key, value) in enumerate(capitals.items()):
    print(i, key, value)
print()

print(list(capitals.keys()).index('TX'))
more_cities = {'VA': 'Richmond', 'NJ': 'Trenton', 'MD': 'Annapolis',
               'NC': 'Raleigh'}
capitals.update(more_cities)
print(capitals)

print(capitals['TX'], capitals['VA'])
print(capitals.get('FL'))
print(capitals.get('SD'))
print(capitals.get('FL', 'NOT FOUND'))
print(capitals.setdefault('FL', 'Tallahassee'))
print(capitals)

print(list(capitals.items()))

for state, capital in capitals.items():
    print(state, capital)
print("-" * 60)

for state, capital in sorted(capitals.items()):
    print(state, capital)
print("-" * 60)

def by_value(element):
    return element[1], element[0]

for state, capital in sorted(capitals.items(), key=lambda e: (e[1], e[0])):
    print(state, capital)
print("-" * 60)

