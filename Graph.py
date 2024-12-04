class Node:
  def __init__(self, hexagon, dimensions=None):
    if (dimensions == None):
      raise ValueError("Dimension not defined") 
  
    self.dimensions = dimensions
    self.visited = False
    self.connections = [[], []]
    self.hexagon = hexagon
    
  def getDimensionIndex(self, dimension):
    # print('getDimensionIndex:',self.hexagon, self.dimensions, dimension)
    return self.dimensions.index(dimension)
  
  def connectNode(self, other):
    otherDimensions = other.dimensions
    commonDimension = [d for d in self.dimensions if d in otherDimensions][0]
    
    selfIndex = [i for i in range(2) if self.dimensions[i] == commonDimension][0]
    otherIndex = [i for i in range(2) if other.dimensions[i] == commonDimension][0]
    
    self.connections[selfIndex].append(other)
    other.connections[otherIndex].append(self)
    
  def isPortal(self):
    return self.dimensions[0] != self.dimensions[1]
    
class Graph:
  def __init__(self, root):
    self.root = root
    
  def drawGraph(self):
    pass
  
  def findPath(self):
    pass