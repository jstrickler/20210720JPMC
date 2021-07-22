mary_in = open('DATA/mary.txt', 'r')   # r means open for reading
# do something with file here ...
mary_in.close()

# mary_in is a file object (like a generator)
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip() # remove trailing \n
        print(line)
print('-' * 60)

with open('/Users/student/Desktop/py3intro2day/DATA/mary.txt') as mary_in:
    all_data = mary_in.read()  # read entire file into one string variable
    print("raw:")
    print(repr(all_data))
    print("normal:")
    print(all_data)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print("-" * 60)

