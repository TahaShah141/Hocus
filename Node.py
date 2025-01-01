from helpers import getOppositeSide

class Node:
  def __init__(self, hexagon, dimensions=None):
    if (dimensions == None):
      raise ValueError("Dimension not defined") 
  
    self.dimensions = dimensions
    self.connections = [[], []]
    self.hexagon = hexagon
  
  def connectNode(self, other, direction, weight):
    otherDimensions = other.dimensions
    commonDimension = [d for d in self.dimensions if d in otherDimensions][0]
    
    selfIndex = [i for i in range(2) if self.dimensions[i] == commonDimension][0]
    otherIndex = [i for i in range(2) if other.dimensions[i] == commonDimension][0]
    
    self.connections[selfIndex].append((other, direction, weight))
    other.connections[otherIndex].append((self, getOppositeSide(direction), weight))
    
    return commonDimension
    
  def isPortal(self):
    return self.dimensions[0] != self.dimensions[1]