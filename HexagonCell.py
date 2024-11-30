from helpers import getOppositeSide
from Graph import Node

class HexagonCell:
  def __init__(self, startDimension=-1, endDimension=-1):
    self.neighbors = [None] * 6
    self.processed = False
    self.overlapSide = -1
    self.nodes = [[Node(self, [d, D]) for d in range(D, 6)] for D in range(6)]
  
  def getNode(self, dimension, otherDimension=None):
    if (otherDimension == None):
      otherDimension = dimension
      
    return self.nodes[min(dimension, otherDimension)][max(dimension, otherDimension)]
    
  
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
  
  def addOverlap(self,  overlapSide):
    self.overlapSide = min(getOppositeSide(overlapSide), overlapSide)
  