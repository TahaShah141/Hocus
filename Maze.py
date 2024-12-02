from helpers import getOppositeSide, getNodeFromLinks

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
      # self.visited[currHex.name].append(nextLink)
      currLinks = currHex.getLinks(currentDimension, enteringSide)
      if (len(currLinks) == 0):
        print(currHex.name, currHex.neighbors, currentDimension, enteringSide)
      
      nextSide, nextDimension = nextLink
      prevSide = getOppositeSide(nextSide)
      nextHex = currHex.neighbors[nextSide]
      nextLinks = nextHex.getLinks(nextDimension, prevSide)
      # print('nextLinks:', nextLinks)
      
      if (len(nextLinks) == 1) or (len(nextLinks) == 2 and nextLinks[0][0] == getOppositeSide(nextLinks[1][0])):
        #two cases: straight line or dead end
        if nextHex.neighbors[nextSide] == None:
          print("-dead end-")
        else:
          found, nextHex = findNextHexagon(nextHex, currentDimension, prevSide)
          if not found:
            print("OTHER DEAD END")
          else: 
            nextLinks = nextHex.getLinks(nextDimension, prevSide)

      
      # Mark the links
      currHex.visitedLinks[currentDimension].append(nextLink)
      nextHex.visitedLinks[nextDimension].append((prevSide, currentDimension))

      # print('currLinks:', currLinks, nextLinks, currHex.endDimension, nextHex.endDimension)
      if len(currLinks) == 0:
        print("Curr Link", len(currLinks), len(nextLinks))
        for hex, LINK in stack:
          print(hex.name, LINK)
      # identify nodes using Links and connect them
      currNode = getNodeFromLinks(currHex, currLinks)
      nextNode = getNodeFromLinks(nextHex, nextLinks)
      # print('nextNode:', nextNode.dimensions)

      currNode.connectNode(nextNode, currentDimension, nextDimension)

      # Add new links to the stack
      newStackLinks = [(nextHex, link) for link in nextLinks if link not in nextHex.visitedLinks[nextDimension]]
      stack += newStackLinks

      # print('\n-------------------------------------------\n')
      # for v in self.visited:
      #   print(v, self.visited[v])
      explore(stack, nextDimension, prevSide)

    # CALL THE RECURSIVE FUNCTION
    explore(stack, currentDimension)
    
  def drawMaze(self):
    pass
  