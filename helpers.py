from enum import Enum

class Dimension(Enum):
  UP = 0
  DOWN = 1
  FRONT = 2
  BACK = 3
  RIGHT = 4
  LEFT = 5

class HexagonSide(Enum):
  TOP = 0
  BOTTOM = 1
  BOTTOM_LEFT = 2
  TOP_RIGHT = 3
  BOTTOM_RIGHT = 4
  TOP_LEFT = 5

def getOppositeSide(side):
  if side == HexagonSide.TOP:
    return HexagonSide.BOTTOM
  if side == HexagonSide.BOTTOM:
    return HexagonSide.TOP
  if side == HexagonSide.BOTTOM_LEFT:
    return HexagonSide.TOP_RIGHT
  if side == HexagonSide.TOP_RIGHT:
    return HexagonSide.BOTTOM_RIGHT
  if side == HexagonSide.BOTTOM_RIGHT:
    return HexagonSide.TOP_LEFT
  if side == HexagonSide.TOP_LEFT:
    return HexagonSide.BOTTOM_LEFT
  
def calculateOptions(hexagon):
  options = [[] for _ in range(6)]
  links = []
  for i in range(6):
    if hexagon.neighbors != None:
      links.append(i)

  if hexagon.overlapSide == -1: #Not Overlap
    for dim in range(6): # Go through all dimensions
      for link in links:
        # check if link or neg-Link
        if link == dim or link == getOppositeSide(dim):
          continue
        options[dim].append((link, dim))
      
      if hexagon.neighbors[dim] != None:
        toAdd = [(y, x) for x, y in options[dim]]
        options[dim] += toAdd
  else:
    # W-X is The Prominent overlap
    W = hexagon.overlapSide
    X = getOppositeSide(W)
    for link in links:
      if link != W and link != X:
        Y = min(Y,link) if Y else link

    Z = getOppositeSide(Y)
    for i in range(6):
      if i not in links:
        A = min(A,link) if A else link
    B = getOppositeSide(A)

    for dim in range(6):
      for link in links:
        # check if link or neg-Link
        if link == dim or link == getOppositeSide(dim):
          continue
        options[dim].append((link, dim))
      
      options[B] += options[W] + options[X]
      options[W].append((W, B))
      options[X].append((X, B))

      options[A] += options[Y] + options[Z]
      options[Y].append((Y, A))
      options[Z].append((Z, A))
  return options


      


      


    

