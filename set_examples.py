colors = ['red', 'blue', 'green']
s = set(colors)
print(s, '\n')

c1 = {'red', 'blue', 'red', 'green', 'red', 'purple', 'pink'}
c2 = {'blue', 'red', 'pink', 'orange', 'brown', 'black'}
c1.add('black')
c1.add('black')
c1.add('black')
print(c1)
print(c2)
print("green" in c1)
print("yellow" in c2)
print("both:", c1 & c2)   # intersection
print("just one:", c1 ^ c2)  # xOR
print("all:", c1 | c2)   # union
print("just c1:", c1 - c2)
print("just c2:", c2 - c1)



