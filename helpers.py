from enum import Enum

class Dimension(Enum):
  UP = 0
  DOWN = 1
  FRONT = 2
  BACK = 3
  RIGHT = 4
  LEFT = 5

class HexagonSide(Enum):
  TOP = 0
  BOTTOM = 1
  BOTTOM_LEFT = 2
  TOP_RIGHT = 3
  BOTTOM_RIGHT = 4
  TOP_LEFT = 5

def getOppositeSide(side):
  if side == HexagonSide.TOP:
    return HexagonSide.BOTTOM
  if side == HexagonSide.BOTTOM:
    return HexagonSide.TOP
  if side == HexagonSide.BOTTOM_LEFT:
    return HexagonSide.TOP_RIGHT
  if side == HexagonSide.TOP_RIGHT:
    return HexagonSide.BOTTOM_RIGHT
  if side == HexagonSide.BOTTOM_RIGHT:
    return HexagonSide.TOP_LEFT
  if side == HexagonSide.TOP_LEFT:
    return HexagonSide.BOTTOM_LEFT

    

