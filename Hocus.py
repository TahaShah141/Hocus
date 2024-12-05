from helpers import *
from Maze import Maze
from Hexagon import HexagonCell

A = HexagonCell(startDimension=0, name="A") # Root
O = HexagonCell(endDimension=2, name="O")   # Goal

B = HexagonCell(name="B")
C = HexagonCell(name="C")
D = HexagonCell(name="D")
E = HexagonCell(name="E")
F = HexagonCell(name="F")
G = HexagonCell(name="G")
H = HexagonCell(name="H")
I = HexagonCell(name="I")
J = HexagonCell(name="J", overlapSide=0)
K = HexagonCell(name="K")
L = HexagonCell(name="L")
M = HexagonCell(name="M")
N = HexagonCell(name="N")

A.addNeighbor(2, B)
A.addNeighbor(1, E)
B.addNeighbor(2, C)
C.addNeighbor(2, D)
C.addNeighbor(4, F)
D.addNeighbor(1, H)
E.addNeighbor(2, F)
E.addNeighbor(1, J)
F.addNeighbor(2, G)
F.addNeighbor(1, K)
G.addNeighbor(2, H)
H.addNeighbor(1, M)
I.addNeighbor(2, J)
I.addNeighbor(1, N)
J.addNeighbor(2, K)
J.addNeighbor(1, O)
K.addNeighbor(2, L)
L.addNeighbor(2, M)
N.addNeighbor(2, O)

MainMaze = Maze(root=A)
MainMaze.buildConnections()
print("-"*50)
path = MainMaze.getSwipePath()