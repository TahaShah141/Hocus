from helpers import getOppositeSide

def printStack(stack):
  for hex, link in stack:
    print(hex.name, link)

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
      if (len(links) == 1) or (len(links) == 2 and links[0][0] == getOppositeSide(links[1][0])):
        nextHexagon = hexagon.neighbors[getOppositeSide(enteringSide)]
        if nextHexagon == None:
          return False, hexagon
        return findNextHexagon(nextHexagon, currentDimension, enteringSide)
      else:
        return True, hexagon
      
    self.visited = {
      "A": [],
      "B": [],
      "C": [],
      "D": [],
      "E": [],
      "F": [],
      "G": [],
      "H": [],
      "I": [],
    }

    def explore(stack, currentDimension, enteringSide=None):

      # Base Case
      if len(stack) == 0:
        return
      
      # Extract Data
      currHex, nextLink = stack.pop()
      # print(currHex.name, nextLink)
      
      self.visited[currHex.name].append(nextLink)
      
      nextSide, nextDimension = nextLink
      prevSide = getOppositeSide(nextSide)
      nextHex = currHex.neighbors[nextSide]
      nextLinks = nextHex.getLinks(nextDimension, prevSide)
      # print('nextLinks:', nextLinks)
      
      if (len(nextLinks) == 1) or (len(nextLinks) == 2 and nextLinks[0][0] == getOppositeSide(nextLinks[1][0])):
        #two cases: straight line or dead end
        if nextHex.neighbors[nextSide] == None:
          print("-dead end-", nextHex.name)
        else:
          found, nextHex = findNextHexagon(nextHex, currentDimension, prevSide)
          if not found:
            print("OTHER DEAD END", nextHex.name)
          else:
            nextLinks = nextHex.getLinks(nextDimension, prevSide)
      
      print(currHex.name, nextLink)
      
      # Mark the links
      currLinkToBan = nextLink
      nextLinkToBan = (prevSide, nextDimension)
      
      currNodeDimensions = currHex.getVisitedLinkDimensions(currLinkToBan)
      nextNodeDimensions = nextHex.getVisitedLinkDimensions(nextLinkToBan)
      
      for d in currNodeDimensions:
        currHex.visitedLinks[d].append(currLinkToBan)
      for d in nextNodeDimensions:
        nextHex.visitedLinks[d].append(nextLinkToBan)
      
      currNode = currHex.getNode(currNodeDimensions)
      nextNode = nextHex.getNode(nextNodeDimensions)
      
      currNode.connectNode(nextNode) 
      
      newStackLinks = [(nextHex, link) for link in nextLinks if link not in nextHex.visitedLinks[nextDimension]]
      stack += newStackLinks

      explore(stack, nextDimension, prevSide)

    # CALL THE RECURSIVE FUNCTION
    explore(stack, currentDimension)
    for d in self.visited:
      print(d, self.visited[d])
    
  def drawMaze(self):
    pass
  