def getOppositeSide(side):
  if side == 0:
    return 1
  if side == 1:
    return 0
  if side == 2:
    return 3
  if side == 3:
    return 2
  if side == 4:
    return 5
  if side == 5:
    return 4
  
def getSideName(side):
  if side == 0:
    return "Top"
  if side == 1:
    return "Bottom"
  if side == 2:
    return "Bottom Left"
  if side == 3:
    return "Top Right"
  if side == 4:
    return "Bottom Right"
  if side == 5:
    return "Top Left"
  
def getAllLinks(hexagon):
  links = [[] for _ in range(6)]
  connections = [i for i in range(6) if hexagon.neighbors[i] != None]
  
  if hexagon.overlapSide == -1: #Not Overlap
    for dim in range(6): # Go through all dimensions
      for connection in connections:
        # check if connection or neg-connection
        if connection == dim or connection == getOppositeSide(dim):
          continue
        links[dim].append((connection, dim))
      
      if hexagon.neighbors[dim] != None:
        toAdd = [(y, x) for x, y in links[dim]]
        links[dim] += toAdd
  elif len(connections) == 4:
    A, B, W, X, Y, Z = hexagon.getLabelledSides()

    for dim in range(6):
      for connection in connections:
        # check if connection or neg-connection
        if connection == dim or connection == getOppositeSide(dim):
          continue
        links[dim].append((connection, dim))
      
    links[B] += links[W] + links[X]
    links[W].append((W, B))
    links[X].append((X, B))

    links[A] += links[Y] + links[Z]
    links[Y].append((Y, A))
    links[Z].append((Z, A))
  else:
    raise ValueError("Incorrect build of Hexagon")
  
  return links

def printPath(path):
  for hex, dims, direction in path[:-1]:
    print((hex.name, dims, direction), end=" -> ")  
  print((path[-1][0].name, path[-1][1]))

