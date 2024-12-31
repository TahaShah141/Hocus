from helpers import getOppositeSide, getSideName
from collections import deque
import json

class Maze:
  def __init__(self, root):
    self.root = root

  def buildConnections(self,createJson = True):

    stack = []
    root = self.root

    currentDimension = root.startDimension
    rootLinks = root.getLinks(currentDimension)

    for links in rootLinks:
      stack.append((root, links))

    def findNextHexagon(hexagon, currentDimension, enteringSide, weight=1):
      links = hexagon.getLinks(currentDimension, enteringSide)
      if hexagon.endDimension != -1:
        print(f"GOAL ON STRAIGHT LINE {hexagon.name}")
        return True, hexagon, weight
        
      if (len(links) == 1) or (len(links) == 2 and links[0][0] == getOppositeSide(links[1][0])):
        nextHexagon = hexagon.neighbors[getOppositeSide(enteringSide)]
        if nextHexagon == None:
          return False, hexagon, weight
        return findNextHexagon(nextHexagon, currentDimension, enteringSide, weight+1)
      else:
        return True, hexagon, weight
      
    self.visited = {}

    def explore(stack, currentDimension, enteringSide=None):

      weight = 1 #default weight
      deadEnd = False

      # Base Case
      if len(stack) == 0:
        return
      
      # Extract Data
      currHex, nextLink = stack.pop()
      nextSide, nextDimension = nextLink
      weight = 1

      while nextLink in currHex.visitedLinks[nextDimension]:
        print("EDGE CASE OF ADDING EXPIRED LINK TO STACK BEFOREHAND")
        if len(stack) == 0:
          return
        currHex, nextLink = stack.pop()
        nextSide, nextDimension = nextLink        
      print(currHex.name, nextLink)
      
      if currHex.name not in self.visited:
        self.visited[currHex.name] = []

      self.visited[currHex.name].append(nextLink)
      
      prevSide = getOppositeSide(nextSide)
      nextHex = currHex.neighbors[nextSide]
      nextLinks = nextHex.getLinks(nextDimension, prevSide)
      # print('nextLinks:', nextHex.name, nextLinks)
      
      if (len(nextLinks) == 1) or (len(nextLinks) == 2 and nextLinks[0][0] == getOppositeSide(nextLinks[1][0])):
        #two cases: straight line or dead end
        if nextHex.neighbors[nextSide] == None:
          print("-dead end-", nextHex.name)
          deadEnd = True
        else:
          found, nextHex, weight = findNextHexagon(nextHex, nextDimension, prevSide)
          # print(found, nextHex.name)
          if not found:
            print("OTHER DEAD END", nextHex.name)
            deadEnd = True

          nextLinks = nextHex.getLinks(nextDimension, prevSide)
      
  
      # Mark the links
      currLinkToBan = (nextSide, nextDimension)
      nextLinkToBan = (prevSide, nextDimension)
      
      currNodeDimensions = currHex.getVisitedLinkDimensions(currLinkToBan)
      nextNodeDimensions = nextHex.getVisitedLinkDimensions(nextLinkToBan)

      # print(currHex.name, currNodeDimensions, nextNodeDimensions)
      
      for d in currNodeDimensions:
        currHex.visitedLinks[d].append(currLinkToBan)
      for d in nextNodeDimensions:
        nextHex.visitedLinks[d].append(nextLinkToBan)
      
      currNode = currHex.getNode(currNodeDimensions)
      nextNode = nextHex.getNode(nextNodeDimensions)
      
      currNode.connectNode(nextNode, nextSide, weight) 

      currNode.connectNode(nextNode, nextSide) 

      if createJson:

        node1Type, node2Type = "regular", "regular"
        if currHex.startDimension != -1 and currHex.startDimension in currNode.dimensions:
          node1Type = "start"
        elif currHex.endDimension != -1 and currHex.endDimension in currNode.dimensions:
          node1Type = "end"
        if nextHex.startDimension != -1 and nextHex.startDimension in nextNode.dimensions:
          node2Type = "start"
        elif nextHex.endDimension != -1 and nextHex.endDimension in nextNode.dimensions:
          node2Type = "end"
        elif deadEnd:
          node2Type = "deadend"
        newEdge = {
          "hex1Name": currHex.name,
          "node1Dim": currNode.dimensions,
          "node1Type": node1Type,
          "hex2Name": nextHex.name, 
          "node2Dim":nextNode.dimensions,
          "node2Type": node2Type,
          "weight": weight
        }
        data.append(newEdge)
      
      newStackLinks = [(nextHex, link) for link in nextLinks if link not in nextHex.visitedLinks[nextDimension]]
      # def uselessCode():
      sameDimLinks = []
      otherLinks = []
      for link in newStackLinks:
        if link[1][1] == currentDimension:
          sameDimLinks.append(link)
        else:
          otherLinks.append(link)

      stack += otherLinks
      stack += sameDimLinks

      if len(stack) == 0:
        return
      # stack += newStackLinks
      nextHex, nextLink = stack[-1]
      nextSide, nextDimension = nextLink
      prevSide = getOppositeSide(nextSide)

      # stack += newStackLinks
      explore(stack, nextDimension, prevSide)

    if createJson:
      fileName='edges.json'
      data=[] #initialize an empty data array which will store edge objects
      with open(fileName, "w") as json_file:
          json.dump(data, json_file, indent=4)

    # CALL THE RECURSIVE FUNCTION
    explore(stack, currentDimension)

    if createJson:
        with open(fileName, "w") as json_file:
          json.dump(data, json_file, indent=4) #push all the updated data into the json file

    for d in self.visited:
      print(d, self.visited[d])
    
  def drawMaze(self):
    pass
  
  def getOptimalPath(self):
        
    visited = set()
    startNode = self.root.getNode([self.root.startDimension])
    queue = deque([startNode])
    visited.add(startNode)
    
    previousNodes = {startNode: None}
    
    while queue:
      node = queue.popleft()
      
      if node.hexagon.endDimension != -1 and node.dimensions == [node.hexagon.endDimension, node.hexagon.endDimension]:
        path = []
        weight = 1
        while node is not None:
          path.append((node.hexagon, node.dimensions, direction, weight))
          prev = previousNodes[node]
          if prev != None:
            node, direction, weight = prev
          else:
            node = None
        return path[::-1]
      
      connections = node.connections[0] + node.connections[1]
      for neighbor, direction, weight in connections:
        if neighbor not in visited:
          visited.add(neighbor)
          previousNodes[neighbor] = (node, direction, weight)
          queue.append(neighbor)
     
  def getSwipePath(self):
    path = self.getOptimalPath()
    if path == None:
      print("NO PATH FOUND")
      return []
    directions = []
    print("START")
    for _hex, _dims, direction, weight in path[:-1]:
      print(getSideName(direction), weight)
      directions.append((direction, weight))
    print("END")
    return directions
    