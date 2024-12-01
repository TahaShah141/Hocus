from helpers import getOppositeSide, getNodeFromLinks

class Maze:
  def __init__(self, root):
    self.root = root

  def buildConnections(self):

    stack = []
    root = self.root

    currentDimension = root.startDimension
    rootLinks = root.getLinks(currentDimension)

    for links in rootLinks:
      stack.append((root, links))

    def findNextHexagon(hexagon, currentDimension, enteringSide):
      links = hexagon.getLinks(currentDimension, enteringSide)
      if len(links) == 1:
        nextHexagon = hexagon.neighbors[getOppositeSide(enteringSide)]
        return findNextHexagon(nextHexagon, currentDimension, enteringSide)
      else:
        return hexagon


    def explore(stack, currentDimension, enteringSide=None):

      # Base Case
      if len(stack) == 0:
        return
      
      # Extract Data
      currHex, nextLink = stack.pop()
      currLinks = currHex.getLinks(currentDimension, enteringSide)
      
      nextSide, nextDimension = nextLink
      prevSide = getOppositeSide(nextSide)
      nextHex = currHex.neighbors[nextSide]
      nextLinks = nextHex.getLinks(nextDimension, prevSide)
      
      if len(nextLinks) == 1:
        nextHex = findNextHexagon(nextHex, nextDimension, prevSide)
        nextLinks = nextHex.getLinks(nextDimension, prevSide)
      
      # Mark the links
      currHex.visitedLinks[currentDimension].append(nextLink)
      nextHex.visitedLinks[nextDimension].append((prevSide, currentDimension))


      # identify nodes using Links and connect them
      currNode = getNodeFromLinks(currHex, currLinks)
      nextNode = getNodeFromLinks(nextHex, nextLinks)

      currNode.connectNode(nextNode, currentDimension)

      # Add new links to the stack
      newStackLinks = [(nextHex, link) for link in nextLinks if link not in nextHex.visitedLinks[nextDimension]]
      stack += newStackLinks

      explore(stack, nextDimension, prevSide)

    explore(stack, currentDimension)
    
  def drawMaze(self):
    pass
  