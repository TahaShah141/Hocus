import { useState, useEffect } from 'react'
// import './App.css'
import DimensionBox from './DimensionBox'
import EdgeLine from './EdgeLine';
import { use } from 'react';
import Node from './Node';

function App() {
  const [edgesJson, setEdgesJson] = useState(null);
  const [dimBoxCoordinates, setDimBoxCoordinates] = useState({
    0: { x: 400, y: 10 },   // Top-center
    1: { x: 400, y: 610 },  // Bottom-center
    2: { x: 50, y: 410 },   // Left-bottom
    3: { x: 750, y: 210 },  // Right-top
    4: { x: 750, y: 410 },  // Right-bottom
    5: { x: 50, y: 210 },   // Left-top
  });
  const [edges, setEdges] = useState([]);
  const [nodes, setNodes] = useState([])
  
  //SETUP FOR NODES AND EDGES
  //sets up EVERYTHING at once
  useEffect(() => {

    //fetching json file upon startup
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

  useEffect(()=>{
    
    if (edgesJson) {
      //temporary dim nodes holder
      const tempNodes = [];
      const tempEdges = [];

      let node1, node1_1, node1_2, node2, node2_1, node2_2, edge1, edge2, edge3, oldNode;

      edgesJson.forEach((edge) => {

        node1 = null, node1_1 = null, node1_2 = null, node2 = null, node2_1 = null, node2_2 = null,
        edge1 = null, edge2 = null, edge3 = null, oldNode=null;


        //extracting nodes 1 and 2 and creating their node objects
        //assigning absoluteX and absoluteY values for each node based on their dimension box
        //initializing edges
        //if the edge is connecting 2 single dimension nodes -> connect node 1 and node 2
        //if the edge is connecting 1 single dimension and 1 portal node -> connect the single dimension with the portal nodes node that is in the same dim box
        //                                                                 AND connect the semi portal nodes together too   
        // if the edge is connecting 2 portal nodes  -> connect portal nodes within same dimBox AND the semi portal nodes of each portal node

        if(isSingleDimension(edge.node1Dim) && isSingleDimension(edge.node2Dim)){

          let dimBox1 = edge.node1Dim[0];

          let [absoluteX1, absoluteY1] = getRandomAbsolute(dimBox1,edge.node1Type)
      
          node1 = {
            "hexName": edge.hex1Name,
            "dimensions": edge.node1Dim,
            "type": edge.node1Type,
            "dimBox": dimBox1,
            "absoluteX": absoluteX1,
            "absoluteY": absoluteY1
          }

          oldNode = doesNodeExist(tempNodes, node1)
          if(oldNode)
            node1=oldNode
          else 
            tempNodes.push(node1)

          let dimBox2 = edge.node2Dim[0];

          let [absoluteX2, absoluteY2] = getRandomAbsolute(dimBox2,edge.node2Type)
      
          node2 = {
            "hexName": edge.hex2Name,
            "dimensions": edge.node2Dim,
            "type": edge.node2Type,
            "dimBox": dimBox2,
            "absoluteX": absoluteX2,
            "absoluteY": absoluteY2
          }

          oldNode = doesNodeExist(tempNodes, node2)
          if(oldNode)
            node2=oldNode
          else 
            tempNodes.push(node2)

          edge1 = {
            ...edge,
            "x1": node1.absoluteX,
            "y1": node1.absoluteY,
            "x2": node2.absoluteX,
            "y2": node2.absoluteY,
            "type": "regular"
          }
          tempEdges.push(edge1);

        }
        else if (!isSingleDimension(edge.node1Dim) && isSingleDimension(edge.node2Dim)){

          let dimBox1 = edge.node1Dim[0]
          
          let [absoluteX1, absoluteY1] = getRandomAbsolute(dimBox1,edge.node1Type)
          // let [absoluteX1_1, absoluteY1_1, absoluteX1_2, absoluteY1_2] = getDimChangeNodePosition(dimBox1, dimBox2)
          
          node1_1 = {
            "hexName": edge.hex1Name,
            "dimensions": edge.node1Dim,
            "type": edge.node1Type,
            "dimBox": dimBox1,
            "absoluteX": absoluteX1,
            "absoluteY": absoluteY1
          }
          
          let oldNode = doesNodeExist(tempNodes, node1_1)
          if(oldNode)
            node1_1=oldNode
          else 
          tempNodes.push(node1_1)
        
        let dimBox2 = edge.node1Dim[1]
        let [absoluteX2, absoluteY2] = getRandomAbsolute(dimBox2,edge.node1Type)

          node1_2 = {
            "hexName": edge.hex1Name,
            "dimensions": edge.node1Dim,
            "type": edge.node1Type,
            "dimBox": dimBox2,
            "absoluteX": absoluteX2,
            "absoluteY": absoluteY2
          }
          
          oldNode = doesNodeExist(tempNodes, node1_2)
          if(oldNode)
            node1_2=oldNode
          else 
            tempNodes.push(node1_2)

          let dimBox3 = edge.node2Dim[0];

          let [absoluteX3, absoluteY3] = getRandomAbsolute(dimBox3,edge.node2Type)
      
          node2 = {
            "hexName": edge.hex2Name,
            "dimensions": edge.node2Dim,
            "type": edge.node2Type,
            "dimBox": dimBox3,
            "absoluteX": absoluteX3,
            "absoluteY": absoluteY3
          }

          oldNode = doesNodeExist(tempNodes, node2)
          if(oldNode)
            node2=oldNode
          else 
            tempNodes.push(node2)

          edge1 = {
            ...edge, // Retain all existing properties
            "x1": node1_1.absoluteX,
            "y1": node1_1.absoluteY,
            "x2": node1_2.absoluteX,
            "y2": node1_2.absoluteY,
            "type": "dotted"
          }
          tempEdges.push(edge1);

          edge2 = {
            ...edge, // Retain all existing properties
            "x1": (node2.dimBox == node1_1.dimBox) ? node1_1.absoluteX : node1_2.absoluteX,
            "y1": (node2.dimBox == node1_1.dimBox) ? node1_1.absoluteY : node1_2.absoluteY,
            "x2": node2.absoluteX,
            "y2": node2.absoluteY,
            "type": "regular"
          }
          tempEdges.push(edge2);
        
        }
        else if(isSingleDimension(edge.node1Dim) && !isSingleDimension(edge.node2Dim)){

          let dimBox1 = edge.node1Dim[0];

          let [absoluteX1, absoluteY1] = getRandomAbsolute(dimBox1,edge.node1Type)
      
          node1 = {
            "hexName": edge.hex1Name,
            "dimensions": edge.node1Dim,
            "type": edge.node1Type,
            "dimBox": dimBox1,
            "absoluteX": absoluteX1,
            "absoluteY": absoluteY1
          }

          oldNode = doesNodeExist(tempNodes, node1)
          if(oldNode)
            node1=oldNode
          else 
            tempNodes.push(node1)

          let dimBox2 = edge.node2Dim[0]
          let [absoluteX2, absoluteY2] = getRandomAbsolute(dimBox2,edge.node2Type)
          
          node2_1 = {
            "hexName": edge.hex2Name,
            "dimensions": edge.node2Dim,
            "type": edge.node2Type,
            "dimBox": dimBox2,
            "absoluteX": absoluteX2,
            "absoluteY": absoluteY2
          }
          
          oldNode = doesNodeExist(tempNodes, node2_1)
          if(oldNode)
            node2_1=oldNode
          else 
            tempNodes.push(node2_1)

          let dimBox3 = edge.node2Dim[1]
          let [absoluteX3, absoluteY3]= getRandomAbsolute(dimBox3,edge.node2Type)

          node2_2 = {
            "hexName": edge.hex2Name,
            "dimensions": edge.node2Dim,
            "type": edge.node2Type,
            "dimBox": dimBox3,
            "absoluteX": absoluteX3,
            "absoluteY": absoluteY3
          }
          
          oldNode = doesNodeExist(tempNodes, node2_2)
          if(oldNode)
            node2_2=oldNode
          else 
            tempNodes.push(node2_2)

          edge1 = {
            ...edge, // Retain all existing properties
            "x1": node2_1.absoluteX,
            "y1": node2_1.absoluteY,
            "x2": node2_2.absoluteX,
            "y2": node2_2.absoluteY,
            "type": "dotted"
          }
          tempEdges.push(edge1);

          edge2 = {
            ...edge, // Retain all existing properties
            "x1": node1.absoluteX,
            "y1": node1.absoluteY,
            "x2": (node1.dimBox == node2_1.dimBox) ? node2_1.absoluteX : node2_2.absoluteX,
            "y2": (node1.dimBox == node2_1.dimBox) ? node2_1.absoluteY : node2_2.absoluteY,
            "type": "regular"
          }
          tempEdges.push(edge2);

        }
        else if(!isSingleDimension(edge.node1Dim) && !isSingleDimension(edge.node2Dim)){
          let dimBox1 = edge.node1Dim[0]
          let [absoluteX1, absoluteY1] = getRandomAbsolute(dimBox1,edge.node1Type)
          
          node1_1 = {
            "hexName": edge.hex1Name,
            "dimensions": edge.node1Dim,
            "type": edge.node1Type,
            "dimBox": dimBox1,
            "absoluteX": absoluteX1,
            "absoluteY": absoluteY1
          }
          
          let oldNode = doesNodeExist(tempNodes, node1_1)
          if(oldNode)
            node1_1=oldNode
          else 
            tempNodes.push(node1_1)
          
          let dimBox2 = edge.node1Dim[1]
          let [absoluteX2, absoluteY2] = getRandomAbsolute(dimBox2,edge.node1Type)

          node1_2 = {
            "hexName": edge.hex1Name,
            "dimensions": edge.node1Dim,
            "type": edge.node1Type,
            "dimBox": dimBox2,
            "absoluteX": absoluteX2,
            "absoluteY": absoluteY2
          }
          
          oldNode = doesNodeExist(tempNodes, node1_2)
          if(oldNode)
            node1_2=oldNode
          else 
            tempNodes.push(node1_2)

          
          let dimBox3 = edge.node2Dim[0]
          let [absoluteX3, absoluteY3] = getRandomAbsolute(dimBox3,edge.node2Type)
          
          node2_1 = {
            "hexName": edge.hex2Name,
            "dimensions": edge.node2Dim,
            "type": edge.node2Type,
            "dimBox": dimBox3,
            "absoluteX": absoluteX3,
            "absoluteY": absoluteY3
          }
          
          oldNode = doesNodeExist(tempNodes, node2_1)
          if(oldNode)
            node2_1=oldNode
          else 
            tempNodes.push(node2_1)

          let dimBox4 = edge.node2Dim[1]
          let [absoluteX4, absoluteY4]= getRandomAbsolute(dimBox4,edge.node2Type)

          node2_2 = {
            "hexName": edge.hex2Name,
            "dimensions": edge.node2Dim,
            "type": edge.node2Type,
            "dimBox": dimBox4,
            "absoluteX": absoluteX4,
            "absoluteY": absoluteY4
          }
          
          oldNode = doesNodeExist(tempNodes, node2_2)
          if(oldNode)
            node2_2=oldNode
          else 
            tempNodes.push(node2_2)

          let a = null
          let b = null
          if (node1_1.dimBox == node2_1.dimBox) {
            a = node1_1; b = node2_1;
          } else if (node1_1.dimBox == node2_2.dimBox) {
              a = node1_1; b = node2_2;
          } else if (node1_2.dimBox == node2_1.dimBox) {
              a = node1_2; b = node2_1;
          } else if (node1_2.dimBox == node2_2.dimBox) {
              a = node1_2; b = node2_2;
          }

          edge1 = {
            ...edge, // Retain all existing properties
            "x1": a.absoluteX,
            "y1": a.absoluteY,
            "x2": b.absoluteX,
            "y2": b.absoluteY,
            "type": "regular"
          }
          tempEdges.push(edge1);
          
        }
        else{
          console.log("ELSE CASE")
        }

        
      });
      
      
      setNodes(tempNodes);
      setEdges(tempEdges);
      console.log('EDGES', edges)
      // console.log('NODES', tempNodes)
    }

  }, [edgesJson])
  
  

  const isSingleDimension = (dimensions) => {
    return dimensions[0] == dimensions[1]
  }
  
  const getRandomAbsolute=(dimBox, nodeType)=>{
    //original x1 and x2 must be 250px away from each other and y1,y2 180
    //some margin is added/subtracted below to avoid rendering at the edges
    let absoluteX, absoluteY;
    if(nodeType == 'start' || nodeType == 'end')
      [absoluteX,absoluteY] =getStartEndNodePosition(dimBox)
    else{
      let x1 = dimBoxCoordinates[dimBox].x+5;
      let y1 = dimBoxCoordinates[dimBox].y;
      let x2 = x1 + 150;
      let y2 = y1 + 120;
      absoluteX = Math.random() * (x2 - x1) + x1;
      absoluteY = Math.random() * (y2 - y1) + y1;
    }
    return [absoluteX, absoluteY];
  }

  function getStartEndNodePosition(dimBox) {
    // Determine the position based on the node type (start or end) and dimension box
    let { x, y } = dimBoxCoordinates[dimBox];

    //centering the node
    x+=110
    y+=75

    // const offset = 10; // Offset to avoid overlapping with the edge of the box
    const offsetX = 90;
    const offsetY = 60;
    switch (dimBox) {
      case 0: 
        return [x, y-offsetY];
      case 1:
        return[x, y + offsetY] ;
      case 2: 
        return[x - offsetX, y+offsetY];
      case 3:
        return [x + offsetX, y-offsetY];
      case 4: 
        return [x + offsetX, y+offsetY];
      case 5:
        return [x - offsetX, y-offsetY];
    }
  }

  // const getDimChangeNodePosition = (dimBox1, dimBox2, node1, node2) => {
  //   // Determine the position based on the node type (start or end) and dimension box
  //   let { x1, y1 } = dimBoxCoordinates[dimBox1];
  //   let { x2, y2} = dimBoxCoordinates[dimBox2];

  //   //centering the nodes
  //   x1+=110
  //   y1+=75
  //   x2+=110
  //   y2+=75

  //   // const offset = 10; // Offset to avoid overlapping with the edge of the box
  //   const offsetX = 90;
  //   const offsetY = 60;

  //   if(dimBox1 == 0)
  //   {
  //     y1=y1+offsetY;
  //     if(dimBox2==2 || dimBox2 == 5)
  //       x1=x1-offsetX;
  //     else if(dimBox2==2 || dimBox2 == 5)
  //       x1=x1+offsetX;
  //   }
  //   else if(dimBox1 == 1){
  //     y1=y1-offsetY;
  //     if(dimBox2==2 || dimBox2 == 5)
  //       x1=x1-offsetX;
  //     else if(dimBox2==2 || dimBox2 == 5)
  //       x1=x1+offsetX;
  //   }
  //   // else if(dimBox)
  //   else if(dimBox1 == 2){
  //     if(dimBox2 == 5){
  //       x1=x1-offsetX;
  //       y1=y1-offsetY;
  //     }
  //     else if(dimBox2 == 0 || dimBox2 == 4){
  //       x1=x1+offsetX;
  //       y1=y1-offsetY;
  //     }
  //     else if(dimBox2 == 1){
  //       x1=x1+offsetX;
  //       y1=y1+offsetY;
  //     }
  //   }
  //   else if(dimBox == 3){
      
  //   }
  //   else if(dimBox == 4){
  //     if(dimBox2 == 1){ //bottom left
  //       x1=x1-offsetX;
  //       y1=y1+offsetY;
  //     }
  //     else if(dimBox2 == 0 || dimBox2 == 2){ //top left
  //       x1=x1-offsetX;
  //       y1=y1-offsetY;
  //     }
  //     else if(dimBox2 == 3){ //top
  //       x1=x1;
  //       y1=y1-offsetY;
  //     }
  //   }
  //   else if(dimBox == 5){

  //   }

  //   return [x1,y1,x2,y2]
  // }

  // findAndUpdateEdgeXY(x1=null, y1=null, x2=null, y2=null){
  //   tempEdges.find(
  //     (e) =>
        
  //   )
  // }

  //to check if node already exists before adding nodes into the node list
  const doesNodeExist = (tempNodes, node) => {
    return tempNodes.find(
      (n) =>
        n.hexName === node.hexName &&
        arraysEqual(n.dimensions, node.dimensions) &&
        n.dimBox === node.dimBox
    ) || null;
  };
  
  const arraysEqual = (arr1, arr2) => {
    if (arr1.length !== arr2.length) return false;
    return arr1.every((val, index) => val === arr2[index]);
  };

  return (
    <>
     <div className="relative w-[1200px] h-[900px] top-0 left-0">
        <DimensionBox id="0" dimNumber={0} dimBoxCoordinates={dimBoxCoordinates}>
        </DimensionBox>
        <DimensionBox id="3" dimNumber={3} dimBoxCoordinates={dimBoxCoordinates}>
        </DimensionBox>
        <DimensionBox id="4" dimNumber={4} dimBoxCoordinates={dimBoxCoordinates}>
        </DimensionBox>
        <DimensionBox id="1" dimNumber={1} dimBoxCoordinates={dimBoxCoordinates}>
        </DimensionBox>
        <DimensionBox id="2" dimNumber={2} dimBoxCoordinates={dimBoxCoordinates}>
        </DimensionBox>
        <DimensionBox id="5" dimNumber={5} dimBoxCoordinates={dimBoxCoordinates}>
        </DimensionBox>
        { nodes ? (nodes.map((node, index) => (
          <Node key={index} node={node}/>
        )))
          : null
        }
        {/* { edges ? (edges.map((edge, index)=>(
            <EdgeLine key={index} x1={edge.x1} y1={edge.y1} x2={edge.x2} y2={edge.y2}></EdgeLine>
          ))) : null
        } */}
        {
          edges? (
            <svg width="100%" height="100%" style={{ position: "absolute", top: 0, left: 0 }}>
              {edges.map((edge, index) => (
                <EdgeLine key={index} x1={edge.x1} y1={edge.y1} x2={edge.x2} y2={edge.y2} type={edge.type}/>
              ))}
            </svg>
          )
          : null
        }
      </div>
      {/* <button className='bg-green-200'>Visualize Graph</button> */}
      <button className="absolute top-1/2 right-11 transform -translate-y-1/2 bg-green-200 p-2">
      Visualize Graph
    </button>
    </>
  )
}

export default App
