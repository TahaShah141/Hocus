from helpers import *
from Maze import Maze
from HexagonCell import HexagonCell

A = HexagonCell(startDimension=Dimension.UP) # Root
H = HexagonCell(endDimension=Dimension.FRONT) # Goal

B = HexagonCell()
C = HexagonCell()
D = HexagonCell()
E = HexagonCell()
F = HexagonCell()
G = HexagonCell()
I = HexagonCell()

A.addNeighbor(HexagonSide.BOTTOM_RIGHT, B) # A-B
A.addNeighbor(HexagonSide.BOTTOM, C) # A-C
B.addNeighbor(HexagonSide.BOTTOM_LEFT, C) # B-C
C.addNeighbor(HexagonSide.BOTTOM_LEFT, D) # C-D
C.addNeighbor(HexagonSide.BOTTOM, E) # C-E
D.addNeighbor(HexagonSide.BOTTOM_RIGHT, E) # D-E
D.addNeighbor(HexagonSide.TOP_LEFT, H) # D-H
D.addNeighbor(HexagonSide.BOTTOM_LEFT, I) # D-I
E.addNeighbor(HexagonSide.BOTTOM_RIGHT, F) # E-F
E.addNeighbor(HexagonSide.BOTTOM, G) # E-G
F.addNeighbor(HexagonSide.BOTTOM_LEFT, G) # F-G
H.addNeighbor(HexagonSide.BOTTOM, I) # H-I

# YET TO DECIDE HOW TO ADD OVERLAP INFORMATION OF HEXAGONS C, D and E (4 neighbors)

TestMaze = Maze(root=A)