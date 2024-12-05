from helpers import getOppositeSide, getAllLinks
from Graph import Node

class HexagonCell:
  def __init__(self, name="", startDimension=-1, endDimension=-1, overlapSide=-1):
    self.neighbors = [None] * 6
    self.visitedLinks = [[] for _ in range(6)]
    self.overlapSide = overlapSide
    self.nodes = [[Node(self, [d, D]) for d in range(D, 6)] for D in range(6)]
    self.startDimension = startDimension
    self.endDimension = endDimension
    self.name = name

  def containsPortal(self, dimension):
    return self.neighbors[dimension] != None
  
  def getVisitedLinkDimensions(self, link):
    links = getAllLinks(self)
    toReturn = []
    for dim in range(6):
      if link in links[dim]:
        toReturn.append(dim)
    return toReturn

  def getLinks(self, currentDimension, enteringSide=None):
    options = getAllLinks(self)

    links = [n for n in self.neighbors if n != None] 
    
    # Straight Line without Overlap
    if len(links) == 2 and links[0] == getOppositeSide(links[1]):
      # Returns only one link
      return [(getOppositeSide(enteringSide), currentDimension)]

    # if not overlap
    if self.overlapSide == -1:
      # Only for starting
      if (enteringSide == None):
        return options[currentDimension]
      return [(x, y) for x, y in options[currentDimension] if enteringSide in (x, y)] if self.containsPortal(currentDimension) else options[currentDimension]

    A, B, W, X, Y, Z = self.getLabelledSides() # 0, 1, 4, 5, 2, 3

    # Filtering according to D and S
    if (currentDimension == A and enteringSide in [Y, Z]) or (currentDimension == B and enteringSide in [W, X]):
        return options[enteringSide] 
    elif currentDimension in [A, B]:
      # returns one link if going through overlap straight line
      return [(getOppositeSide(enteringSide), currentDimension)]
    else:
      return options[currentDimension]      

  def getNode(self, dimensions):
    if len(dimensions) == 1:
      return self.nodes[dimensions[0]][0]
    lesser, greater = min(dimensions), max(dimensions)
    return self.nodes[lesser][greater - lesser]
    
  def getLabelledSides(self):
    links = [i for i in range(6) if self.neighbors[i] != None]
    
    W = self.overlapSide
    X = getOppositeSide(W)
    A = B = Y = Z = None
    
    for link in links:
      if link != W and link != X:
        Y = min(Y,link) if Y != None else link

    Z = getOppositeSide(Y)
    for i in range(6):
      if i not in links:
        A = min(A, i) if A != None else i
    B = getOppositeSide(A)

    return A, B, W, X, Y, Z

  def addNeighbor(self, side, neighbor):
    self.neighbors[side] = neighbor
    neighbor.neighbors[getOppositeSide(side)] = self
  
def makeHexagon(links, dash=-1):
  hexagons = [None]*6
  for link in links:
    hexagons[link] = HexagonCell()

  toReturn = HexagonCell()
  if dash != -1:
    # toReturn.addOverlap(dash)
    toReturn.overlapSide = dash

  toReturn.neighbors = hexagons

  return toReturn