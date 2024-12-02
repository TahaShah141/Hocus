from helpers import getAllLinks
from Hexagon import makeHexagon

hexA = makeHexagon([3, 1])
optsA = getAllLinks(hexA)
optionsA = hexA.getLinks(currentDimension=0, enteringSide=3)

for o in range(6):
    print(o, optsA[o])
print()
print(optionsA)
print()

# hexB = makeHexagon([0, 1, 2, 3], 0)
# optsB = getAllLinks(hexB)
# optionsB = hexB.getLinks(currentDimension=0, enteringSide=3)

# for o in range(6):
#     print(o, optsA[o])
# print()
# print(optionsB)
# print()


'''
At B we chose (2, 0) with D = 0 and S = 5
At (2, 0) lies hex C.

to connect:
00B -- 05C
'''