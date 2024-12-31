import { useState, useEffect } from 'react'
import './App.css'

function DimensionBox({id, dimNumber, dimBoxCoordinates}) {
  // const [nodeCount, setNodeCount] = useState(0)
  const [outlineColor, setOutlineColor] = useState('orange')
  
  useEffect(()=>{
    if (['2', '3'].includes(id)) {
      setOutlineColor('lightblue');
    } else if (['5', '4'].includes(id)) {
      setOutlineColor('black');
    }
  })
  
  return (
    <div  
      id={id}
      className="absolute w-[250px] h-[180px] grid grid-rows-6 grid-cols-6 border-2 rounded-md"
      style={{
        top: `${dimBoxCoordinates[parseInt(id)].y}px`,
        left: `${dimBoxCoordinates[parseInt(id)].x}px`,
        borderColor: outlineColor,
        position: 'absolute',
      }}
    >
      <p>{`Dim ${dimNumber}`}</p>
      {/* {nodes ? (
        nodes.map((node, index) => (
          <Node key={index} dimBoxId={id} dimensions={node.dimensions} type={node.type} hexName={node.name} gridRow={node.gridRow} gridColumn={node.gridColumn} node={node} onPositionUpdate={onPositionUpdate}/>
        ))
      ) : null} */}
    </div>
  )
}

export default DimensionBox
