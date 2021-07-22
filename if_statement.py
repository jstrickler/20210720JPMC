import sys

value = 80

if value > 75:
    print("wombat")
    print("wallaby")
    if value > 60:
        print("great white shark")
elif value > 50:  # else if
    print("kangaroo")
    print("kookaburra")
else:
    print("platypus")
    print("quokka")

print("Done.")

x = ""
if x:
    print("Walla Walla Washington")



# if else elif while for with try except finally def class

#  x is False if
#  x is number and x == 0
#  x is None
#  x is a container and len(x) == 0    ""  []  {}  set() ()

# x is True if
# x != 0
# len(x) > 0

debug = True
#  color = debug ? "red" : "green";

color  = "red" if debug else "green"

if debug:
    color = "red"
else:
    color = "green"

#  == != > < >= <=
#  <> not used

if color is "red":
    pass

if color is None:
    pass

#  and or not

# NOT USED IN PYTHON: && || !
#  & | ~ are used for bits

if (value > 50) and (value < 100):
    print("wahoooo")

if len(sys.argv) > 1:
    value = float(sys.argv[1])
else:
    print("Please specify a value on the command line")
    sys.exit()












