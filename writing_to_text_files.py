fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        line = fruit + '\n'
        fruits_out.write(line)

with open('DATA/words.txt') as words_in:
    with open('qwords.txt', 'w') as qwords_out:
        with open('xwords.txt', 'w') as xwords_out:
            for line in words_in:
                if line.startswith('q'):
                    qwords_out.write(line)
                elif line.startswith('x'):
                    xwords_out.write(line)




