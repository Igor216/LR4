#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

# Реализация задания 2
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
test=Unique(data1)
for i in test:
    print(i, end=',')

print("\n")
data2 = gen_random(1,3,10)
test = Unique(data2)
for i in test:
	print(i, end=',')


