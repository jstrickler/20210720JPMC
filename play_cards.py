from carddeck import CardDeck

d1 = CardDeck("Abigail")
d2 = CardDeck("Robert")
print(d1, d2)

print(d1.dealer)
print(d2.dealer)

d1.dealer = "Charlotte"
print(d1.dealer)
# d1.shuffle()
# print(d1.draw())

try:
    d1.dealer = 12.34
except TypeError as err:
    print(err)
else:
    print("dealer is", d1.dealer)

d1.shuffle()
print(d1.cards)
for i in range(10):
    print(d1.draw())

d1.waddle()
d1.coo()

print(CardDeck.mro())

