import { useState, useEffect } from 'react'
// import './App.css'
import DimensionBox from './DimensionBox'
import EdgeLine from './EdgeLine';
import { use } from 'react';

class Node {
  constructor(name, type, dimensions,gridRow=-1, gridColumn=-1) {
    this.name = name;
    this.type =type;
    this.dimensions = dimensions;
    this.gridRow = gridRow
    this.gridColumn = gridColumn;
    this.absoluteX=-1;
    this.absoluteY=-1;
  }

  isSingleDimension() {
    return this.dimensions[0] === this.dimensions[1];
  }

  // addPosition(gridPosition){
  //   this.gridPosition = gridPosition;
  // }
  addPosition(gridRow, gridColumn){
    this.gridRow = gridRow;
    this.gridColumn = gridColumn;
  }
  setAbsolutePosition(X,Y){
    this.absoluteX = X;
    this.absoluteY = Y;
  }
}

class Edge {
  constructor(node1, node2, edgeType, weight, x1=-1, y1=-1, x2=-1, y2=-1){
    this.node1 = node1;
    this.node2= node2;
    this.edgeType = edgeType;
    this.weight=weight;
  }
}

function App() {
  const [edgesJson, setEdgesJson] = useState(null);
  const [edges, setEdges] = useState([]);
  const [dimNodes, setDimNodes] = useState({
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
  });
  const [arePositionsUpdated, setArePositionsUpdated] = useState(false);
  // console.log(dimNodes[5])
  
  //fetching json file upon startup
  useEffect(() => {
    fetch('edges.json')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((jsonData) => {
      setEdgesJson(jsonData);
    })
    .catch((err) => {
      console.error('Error fetching JSON:', err);
    });
  }, []);
  
  //everytime edges changes, parse through all nodes
  useEffect(() => {
    if (edgesJson) {
      //temporary dim nodes holder
      const tempDimNodes = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
      };
      const tempEdges = [];

      edgesJson.forEach((edge) => {
        //extracting nodes 1 and 2 and adding it to the relevant dimension node lists
        const node1 = new Node(edge.hex1Name, edge.node1Type, edge.node1Dim);
        addNodeToTempDimNodes(tempDimNodes, node1);
        const node2 = new Node(edge.hex2Name, edge.node2Type, edge.node2Dim);
        addNodeToTempDimNodes(tempDimNodes, node2);

        const edgeType = "regular";
        const weight = 1;
        const edgeObject = new Edge(node1, node2, edgeType, weight);
        console.log(edgeObject)
        tempEdges.push(edgeObject);
      });

      setDimNodes(tempDimNodes);
      setEdges(tempEdges);

      // let edgeType = (node1.isSingleDimension & node2.isSingleDimension) ? "regular" : "portal"
      // const edgeObject = new Edge(node1, node2, edgeType)
   

      //all nodes have been added by this point
      //update the grid positions for all node objects created based on the number of nodes present in each dimension list

      //temp fix by placing all on diagonal (smth still wrong w placement though)
      for (let k = 0; k < 6; k++) {
        const dimList = tempDimNodes[k];
        if (dimList.length === 0) continue;
        const gridRows = 6;
        const gridCols = 8;
        const gap = 1;
      
        let currentIndex = 1;
        dimList.forEach((node, index) => {
          const gridRow = currentIndex;
          const gridCol = currentIndex;
          node.addPosition(gridRow, gridCol);
      
          // Debugging output
          if (k === 0) {
            console.log(`Node ${index} -> Row: ${gridRow}, Column: ${gridCol}, Node Object: `, node);
          }
          currentIndex += gap;
          if (currentIndex > Math.min(gridRows, gridCols)) {
            return;
          }
        });
      }

    }
  }, [edgesJson]); 

  const handleNodePositionUpdate = (updatedNode, dimBox) => {
    setDimNodes((prevDimNodes) => {
      // Create a copy of the previous dimNodes state to avoid direct mutation
      const updatedDimNodes = { ...prevDimNodes };
  
      // Check if the provided dimBox ID exists in the state
      if (updatedDimNodes[dimBox]) {
        // Update the node in the relevant dimension array
        updatedDimNodes[dimBox] = updatedDimNodes[dimBox].map((node) =>
          node.name === updatedNode.name ? updatedNode : node
        );
      }
  
      // Return the updated state
      return updatedDimNodes;
    });

    setEdges((prevEdges) => {
      const updatedEdges = prevEdges.map((edge) => {
        // Check if updatedNode matches node1 or node2 in the edge
        if (edge.node1.name === updatedNode.name && edge.node1.dimensions === updatedNode.dimensions) {
          edge.node1 = updatedNode;
          console.log("UPDATED EDGE NODE1")
        }
        if (edge.node2.name === updatedNode.name && edge.node2.dimensions === updatedNode.dimensions) {
          // Update only node2 if it matches
          edge.node2 = updatedNode
          console.log("UPDATED EDGE NODE2")
        }
        return edge;
      });
      return updatedEdges; // Return the updated edges array
    });
  };

  const addNodeToTempDimNodes = (tempDimNodes, node) => {
    const addNodeToDimension = (dim, node) => {
      if (!tempDimNodes[dim].some((n) => n.name === node.name)) {
        tempDimNodes[dim].push(node);
      }
    };

    if (node.isSingleDimension()) {
      addNodeToDimension(node.dimensions[0], node);
    } else {
      addNodeToDimension(node.dimensions[0], node);
      addNodeToDimension(node.dimensions[1], node);
    }
  };

  return (
    <>
     <div className="relative w-[800px] h-[700px] top-0 left-0">
        <DimensionBox id="0" positioning="top-0 left-1/2 transform -translate-x-1/2" dimNumber={0} nodes={dimNodes[0]} onPositionUpdate={handleNodePositionUpdate}>
          {dimNodes[0].forEach((dim0Node)=>{
            return <Node></Node>
          })}
        </DimensionBox>
        <DimensionBox id="3" positioning="top-1/3 right-0 transform -translate-y-1/2" dimNumber={3} nodes={dimNodes[3]} onPositionUpdate={handleNodePositionUpdate}>
          {dimNodes[3].forEach((dim0Node)=>{
            return <Node></Node>
          })}
        </DimensionBox>
        <DimensionBox id="4" positioning="top-2/3 right-0 transform -translate-y-1/2" dimNumber={4} nodes={dimNodes[4]} onPositionUpdate={handleNodePositionUpdate}>
          {dimNodes[4].forEach((dim0Node)=>{
            return <Node></Node>
          })}
        </DimensionBox>
        <DimensionBox id="1" positioning="bottom-0 left-1/2 transform -translate-x-1/2" dimNumber={1} nodes={dimNodes[1]} onPositionUpdate={handleNodePositionUpdate}>
          {dimNodes[1].forEach((dim0Node)=>{
            return <Node></Node>
          })}
        </DimensionBox>
        <DimensionBox id="2" dimNumber={2} positioning="top-2/3 left-0 transform -translate-y-1/2" nodes={dimNodes[2]} onPositionUpdate={handleNodePositionUpdate}>
          {dimNodes[2].forEach((dim0Node)=>{
            return <Node></Node>
          })}
        </DimensionBox>
        <DimensionBox id="5" dimNumber={5} positioning="top-1/3 left-0 transform -translate-y-1/2" nodes={dimNodes[5]} onPositionUpdate={handleNodePositionUpdate}>
          {dimNodes[5].forEach((dim0Node)=>{
            return <Node></Node>
          })}
        </DimensionBox>

        <svg width="100%" height="100%" style={{ position: "absolute", top: 0, left: 0 }}>
          {edges.map((edge, index) => (
            <EdgeLine key={index} node1={edge.node1} node2={edge.node2} />
          ))}
        </svg>
      </div>
      {/* <button className='bg-green-200'>Visualize Graph</button> */}
      <button className="absolute top-1/2 right-11 transform -translate-y-1/2 bg-green-200 p-2">
      Visualize Graph
    </button>
    </>
  )
}

export default App
