# my @stuff;    print "$stuff[0]\n";
import sys
import typing as T

list1 = list()  # empty
list2 = ['spam', 'ham', 'toast', 'bacon']
list3 = [1, 'wombat', None, ['more', 'stuff']]
list4: T.List[float] = []   # type HINT (ignored by interpreter)

def spam(values: T.Iterable[int]) -> float:
    pass

list4.append("hello")
list4.append(None)
print(list4, '\n')
#  Pandas dataframe  2dim
# numpy ndarray    n-dim of the SAME numeric type

cities = []
cities.insert(2, 'Houston')
print(cities)
cities.append('Chicago')
print(cities)
cities.append('NYC')
print(cities)
cities.insert(0, 'Detroit')
cities.insert(2, 'Miami')
print(cities)
cities.insert(0, 'Durham')
print(cities)
cities.insert(99, 'Chapel Hill')
print(cities)
pos = cities.index('Miami')
print(f"Miami is at index {pos}")
more_cities = ['Des Moines', 'Toledo', 'Salt Lake City']
cities.extend(more_cities)  # add each element of iterable individually
print(cities[7])
print(cities[7][1])   # cities[7,1] only in numpy
print(cities)
print(len(cities), type(cities))
x = 5
del cities[0]
del x
print(cities)
c = cities.pop()  # default pos is -1
print(c, cities)
c = cities.pop(2)
print(c, cities)

cities2 = cities  #   adds 'cities2' as 2nd name for list obj
del cities
print(cities2)
cities3 = cities2
cities3.append('Sacramento')
print(cities2)
cities = list(cities3)  # create NEW list from cities3 (shallow copy)
cities3.append('Portland')
print(cities)

import copy
cities4 = copy.deepcopy(cities)  # make recursive copy

cities.remove('Toledo')
print(cities)
print('NYC' in cities)
print('Minneapolis' in cities)

cities.append('Pittsburgh')
cities.append('Albany')
cities.append('Santa Fe')
cities.append('Montgomery')
print(len(cities), cities)
print(cities[0])
print(cities[10])
print(cities[-2])  #  cities[len(cities)-2]
city = "Tallahassee"
cities.append(city)
print(cities)
del city
print(cities)

print("3:7", cities[3:7])
print(cities[0:3])
print(cities[:3])
print(cities[-5:])

state = "Minnesota"
print(state[:3], state[1:4], state[-4:])

x = "This is a test. This is only a test of the Python educational system"
#  x[start:stop:step]    x[0:len(x):1]
print(x[::2])
print(x[1::2])
print(x[::3])

raw_line = "'Twas brillig and the slithy toves\n"
line = raw_line.rstrip()

args = sys.argv[1:]   # all but the first element
print("sys.argv:", sys.argv)
print("args:", args)
print()
print(cities, '\n')

for i, city in enumerate(cities):
    # city = <next-element-of>(cities)
    print(i, city, len(city), city[:3].upper())
print()












