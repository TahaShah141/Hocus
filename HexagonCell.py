from helpers import getOppositeSide
from Graph import Node

class HexagonCell:
  def __init__(self, startDimension=-1, endDimension=-1):
    self.neighbors = [None] * 6
    self.processed = False
    self.overlapSide = -1
    self.nodes = [[Node(self, [d, D]) for d in range(D, 6)] for D in range(6)]
  
  def addNeighbor(self, side, neighbor):
    self.neighbors[side] = neighbor
    neighbor.neighbors[getOppositeSide(side)] = self
  
  def addOverlap(self,  overlapSide):
    self.overlapSide = min(getOppositeSide(overlapSide), overlapSide)
  