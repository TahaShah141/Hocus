from helpers import *
from Maze import Maze
from Hexagon import HexagonCell

A = HexagonCell(startDimension=0, name="A") # Root
H = HexagonCell(endDimension=2, name="H") # Goal

B = HexagonCell(name="B")
C = HexagonCell(name="C")
D = HexagonCell(name="D")
E = HexagonCell(name="E")
F = HexagonCell(name="F")
G = HexagonCell(name="G")
I = HexagonCell(name="I")

A.addNeighbor(4, B) # A-B
A.addNeighbor(1, C) # A-C
B.addNeighbor(2, C) # B-C
C.addNeighbor(2, D) # C-D
C.addNeighbor(1, E) # C-E
D.addNeighbor(4, E) # D-E
D.addNeighbor(5, H) # D-H
D.addNeighbor(2, I) # D-I
E.addNeighbor(4, F) # E-F
E.addNeighbor(1, G) # E-G
F.addNeighbor(2, G) # F-G
H.addNeighbor(1, I) # H-I

C.addOverlap(0)
D.addOverlap(2)
E.addOverlap(0)

TestMaze = Maze(root=A)
TestMaze.buildConnections()