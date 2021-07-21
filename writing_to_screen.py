a = 10
b = "wombat"
c = 28.23902393

print(a)   #  print(str(a) + '\n')
print(a, b)   # print(str(a) + ' ' + str(b) + '\n')

print(repr(b))
print(a, b, c, sep=":")
print(a, b, c, sep="//")
print(a, b, c, sep="")
print(a,b,c)
print(5+4)
print(a)
print(b)
print(c)
print(a, end="-->")  # sep is still ' '
print(b, end="")
print(c)
print(a, b, c, sep=' ', end='\n')  # defaults
print(a, b, c)  # same as previous
# print(str(a) + sep + str(b) + sep + str(c) + end)
print(a, b, c, sep="")

print("a is", a, "b is", b, "c is", c)
print("a is {} b is {} c is {:.2f}".format(a, b, c))
print(f"a is {a} b is {b} c is {c}")   #  python version 3.6+

print(f"a is {a:4d} b is {b} c is {c:.2f}")   #  python version 3.6+
print(f"a is {a:04d} b is {b} c is {c:.2f}")   #  python version 3.6+
x = 2_032_804_928_340_820
print(f"{x:,d}")

# print(1_0 * 5_0.0)

e = "Python"
f = "rocks"
print(f"{e} {f}!")
