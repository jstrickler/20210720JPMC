
i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("What is your name? (q to quit) ")
    if name == 'q':
        break  # exit loop
    if name == '':
        continue  # go to top of loop
    print("Hello,", name)
