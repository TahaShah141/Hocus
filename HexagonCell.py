from helpers import getOppositeSide

class HexagonCell:
  def __init__(self, startDimension=-1, endDimension=-1):
    self.neighbors = [None] * 6
    self.processed = False
  
  def addNeighbor(self, side, neighbor):
    self.neighbors[side] = neighbor
    neighbor.neighbors[getOppositeSide(side)] = self
  