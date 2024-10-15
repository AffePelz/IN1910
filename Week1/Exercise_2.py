import random
from operator import itemgetter

deck = []
for number in range(1, 14):
    for suit in ["C", "D", "H", "S"]:
        deck.append((number, suit))

random.shuffle(deck)

d = sorted(deck[1:14], key=itemgetter(1, 0))
for i in d:
    print(i)
