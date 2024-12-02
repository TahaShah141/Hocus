from helpers import getOppositeSide, getAllLinks
from Graph import Node

class HexagonCell:
  def __init__(self, name="", startDimension=-1, endDimension=-1):
    self.neighbors = [None] * 6
    self.visitedLinks = [[] for _ in range(6)]
    self.overlapSide = -1
    self.nodes = [[Node(self, [d, D]) for d in range(D, 6)] for D in range(6)]
    self.startDimension = startDimension
    self.endDimension = endDimension
    self.name = name

  def containsPortal(self, dimension):
    return self.neighbors[dimension] != None

  def getLinks(self, currentDimension, enteringSide=None):
    options = getAllLinks(self)

    links = [n for n in self.neighbors if n != None] 

    if len(links) == 2 and links[0] == getOppositeSide(links[1]):
      return [(getOppositeSide(enteringSide), currentDimension)]

    if self.overlapSide == -1:
      if (enteringSide == None):
        return options[currentDimension]
      return [(x, y) for x, y in options[currentDimension] if enteringSide in (x, y)] if self.containsPortal(currentDimension) else options[currentDimension]

    A, B, W, X, Y, Z = self.getLabelledSides() # 0, 1, 4, 5, 2, 3

    # Filtering according to D and S
    if (currentDimension == A and enteringSide in [Y, Z]) or (currentDimension == B and enteringSide in [W, X]):
        return options[enteringSide] 
    elif currentDimension in [A, B]:
      return [(getOppositeSide(enteringSide), currentDimension)]
    else:
      return options[currentDimension]      

    
  
  def getNode(self, dimension, otherDimension=None):
    if (otherDimension == None):
      otherDimension = dimension

    lesser, greater = min(dimension, otherDimension), max(dimension, otherDimension)    
    return self.nodes[lesser][greater-lesser]
    
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

  
  def connectHexagon(self, other, dimension): 
    selfNode = None
    if (self.neighbors[dimension] == None):
      selfNode = self.getNode(dimension)
    else:
      otherSide = getHexagonSide(other)
      selfNode = self.getNode(dimension, otherSide)
    
    otherNode = None
    if (other.neighbors[dimension] == None):
      otherNode = other.getNode(dimension)
    else:
      selfSide = other.getHexagonSide(self)
      otherNode = other.getNode(otherSide, selfSide)
    
    selfNode.connectNode(dimension, otherNode)
   
    def getHexagonSide(self, other):
      return self.neighbors.index(other)
    
  def addNeighbor(self, side, neighbor):
    self.neighbors[side] = neighbor
    neighbor.neighbors[getOppositeSide(side)] = self
  
  def addOverlap(self, overlapSide):
    self.overlapSide = min(getOppositeSide(overlapSide), overlapSide)
  
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