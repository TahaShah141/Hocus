class Node:
  def __init__(self, hexagon, dimensions=None):
    if (dimensions == None):
      raise ValueError("Dimension not defined") 
  
    self.dimensions = dimensions
    self.visited = False
    self.connections = [[], []]
    self.hexagon = hexagon
    
  def getDimensionIndex(self, dimension):
    print(self.hexagon, self.dimensions, dimension)
    return self.dimensions.index(dimension)
  
  def connectNode(self, other, dimension):
    index = self.getDimensionIndex(dimension)
    otherIndex = other.getDimensionIndex(dimension)
    self.connections[index].append(other)
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