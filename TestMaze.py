# from helpers import *
# from Maze import Maze
# from Hexagon import HexagonCell

# A = HexagonCell(startDimension=0, name="A") # Root
# H = HexagonCell(endDimension=2, name="H") # Goal

# B = HexagonCell(name="B")
# C = HexagonCell(name="C", overlapSide=0)
# D = HexagonCell(name="D", overlapSide=2)
# E = HexagonCell(name="E", overlapSide=0)
# F = HexagonCell(name="F")
# G = HexagonCell(name="G")
# I = HexagonCell(name="I")

# A.addNeighbor(4, B) # A-B
# A.addNeighbor(1, C) # A-C
# B.addNeighbor(2, C) # B-C
# C.addNeighbor(2, D) # C-D
# C.addNeighbor(1, E) # C-E
# D.addNeighbor(4, E) # D-E
# D.addNeighbor(5, H) # D-H
# D.addNeighbor(2, I) # D-I
# E.addNeighbor(4, F) # E-F
# E.addNeighbor(1, G) # E-G
# F.addNeighbor(2, G) # F-G
# H.addNeighbor(1, I) # H-I

# TestMaze = Maze(root=A)
# TestMaze.buildConnections()

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

TestMaze = Maze(root=A)
TestMaze.buildConnections()

