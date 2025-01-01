import { useRef, useEffect } from 'react';

export const Graph = ({ json }) => {
  const { nodes, edges } = json;

  const Nodes = [new Set(), new Set(), new Set(), new Set(), new Set(), new Set()];
  const portals = [];
  const nodeCoordinates = useRef({}); // Use a ref to store the coordinates

  // Define bright colors for borders and nodes
  const colors = ['#FF5733', '#33FF57', '#5733FF', '#FF33FF', '#33FFF5', '#FFD700'];

  // Process nodes
  for (const node of nodes) {
    const [hexI, hexJ, dim1, dim2] = node.split('-');
    Nodes[dim1].add(`${hexI}-${hexJ}`);

    if (dim1 !== dim2) {
      Nodes[dim2].add(`${hexI}-${hexJ}`);
      portals.push([`${hexI}-${hexJ}`, dim1, dim2]);
    }
  }

  console.log('Portals:', portals);

  // Transform edges
  const transformEdges = (edges) => {
    return edges.map(([node1, node2, weight]) => {
      const transformedNode1 = node1.split('-').slice(0, 2).concat(weight).join('-');
      const transformedNode2 = node2.split('-').slice(0, 2).concat(weight).join('-');
      return [transformedNode1, transformedNode2];
    });
  };

  const transformedEdges = transformEdges(edges);

  // Convert sets to arrays for rendering
  const NodesArray = Nodes.map((set) => Array.from(set));

  useEffect(() => {
    console.log('Node Coordinates:', nodeCoordinates.current);
  }, []);

  const distributeNodes = (boxX, boxY, boxSize, numNodes) => {
    const positions = [];
    const padding = 20;
    const availableSize = boxSize - 2 * padding;

    const cx = boxX + boxSize / 2;
    const cy = boxY + boxSize / 2;

    const radius = availableSize / 2;

    for (let i = 0; i < numNodes; i++) {
      const angle = (i * Math.PI * 2) / (numNodes);
      const x = cx + radius * Math.cos(angle);
      const y = cy + radius * Math.sin(angle);
      positions.push({ x, y });
    }


    // const rows = Math.ceil(Math.sqrt(numNodes));
    // const cols = Math.ceil(numNodes / rows);

    // const xSpacing = availableSize / cols;
    // const ySpacing = availableSize / rows;

    // let count = 0;
    // for (let row = 0; row < rows && count < numNodes; row++) {
    //   for (let col = 0; col < cols && count < numNodes; col++) {
    //     const x = boxX + padding + col * xSpacing + xSpacing / 2;
    //     const y = boxY + padding + row * ySpacing + ySpacing / 2;
    //     positions.push({ x, y });
    //     count++;
    //   }
    // }

    return positions;
  };

  return (
    <canvas
      ref={(canvasRef) => {
        if (!canvasRef) return;
        const ctx = canvasRef.getContext('2d');
  
        if (ctx) {
          // Clear the canvas
          ctx.clearRect(0, 0, canvasRef.width, canvasRef.height);
  
          // Set dimensions and center
          const canvasWidth = canvasRef.width;
          const canvasHeight = canvasRef.height;
          const boxSize = 150;
          const hexRadius = 300;
  
          // Hexagonal arrangement angles
          const angles = [
            270, // Top (0)
            90,  // Bottom (1)
            150, // Bottom Left (2)
            330, // Top Right (3)
            30,  // Bottom Right (4)
            210, // Top Left (5)
          ].map((angle) => (angle * Math.PI) / 180);
  
          // Calculate box positions
          const boxPositions = angles.map((angle) => {
            const x = canvasWidth / 2 + hexRadius * Math.cos(angle) - boxSize / 2;
            const y = canvasHeight / 2 + hexRadius * Math.sin(angle) - boxSize / 2;
            return { x, y };
          });
  
          // Count edges for each node
          const edgeCounts = {};
          transformedEdges.forEach(([node1, node2]) => {
            edgeCounts[node1] = (edgeCounts[node1] || 0) + 1;
            edgeCounts[node2] = (edgeCounts[node2] || 0) + 1;
          });
  
          // Draw Nodes in Boxes
          NodesArray.forEach((layer, layerIndex) => {
            const { x: boxX, y: boxY } = boxPositions[layerIndex];
  
            // Draw box with border color
            ctx.strokeStyle = colors[layerIndex];
            ctx.lineWidth = 4;
            ctx.strokeRect(boxX, boxY, boxSize, boxSize);
  
            const positions = distributeNodes(boxX, boxY, boxSize, layer.length);
  
            layer.forEach((node, index) => {
              const { x, y } = positions[index];
  
              // Save coordinates for edges
              const key = `${node}-${layerIndex}`;
              nodeCoordinates.current[key] = { x, y };
  
              // Check if the node is a portal
              const isPortal = portals.some(
                ([portalNode]) => portalNode === node
              );
  
              // Check if the node has only one edge
              const isSingleEdge = edgeCounts[key] === 1;
  
              // Draw node with appropriate color
              ctx.fillStyle = isSingleEdge && !isPortal ? 'darkred' : colors[layerIndex];
              ctx.beginPath();
              ctx.arc(x, y, 10, 0, Math.PI * 2);
              ctx.fill();
  
              // Add a white dot for portal nodes
              if (isPortal) {
                ctx.fillStyle = '#3e7568';
                ctx.beginPath();
                ctx.arc(x, y, 4, 0, Math.PI * 3);
                ctx.fill();
              }
  
              // Draw text
              ctx.fillStyle = '#fff';
              ctx.font = '12px Arial';
              // ctx.fillText(key, x - 15, y - 15);
            });
          });
  
          // Draw Edges
          transformedEdges.forEach(([node1, node2]) => {
            const coord1 = nodeCoordinates.current[node1];
            const coord2 = nodeCoordinates.current[node2];
  
            if (coord1 && coord2) {
              ctx.beginPath();
              ctx.moveTo(coord1.x, coord1.y);
              ctx.lineTo(coord2.x, coord2.y);
              ctx.strokeStyle = '#ccc';
              ctx.lineWidth = 2;
              ctx.stroke();
            }
          });
  
          // Draw Portal Edges (Dotted Lines)
          portals.forEach(([start, dim1, dim2]) => {
            const startKey = `${start}-${dim1}`;
            const endKey = `${start}-${dim2}`;
            const coord1 = nodeCoordinates.current[startKey];
            const coord2 = nodeCoordinates.current[endKey];
  
            if (coord1 && coord2) {
              ctx.beginPath();
              ctx.moveTo(coord1.x, coord1.y);
              ctx.lineTo(coord2.x, coord2.y);
              ctx.strokeStyle = '#999';
              ctx.lineWidth = 1;
              ctx.setLineDash([5, 5]); // Dotted line
              ctx.stroke();
              ctx.setLineDash([]); // Reset line style
            }
          });
        }
      }}
      width={800}
      height={800}
      className="rounded-md border"
    />
  );
  
};
