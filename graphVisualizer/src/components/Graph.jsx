import { useRef, useEffect } from 'react';

export const Graph = ({ json }) => {
  const { nodes, edges } = json;

  const Nodes = [new Set(), new Set(), new Set(), new Set(), new Set(), new Set()];
  const portals = [];
  const nodeCoordinates = useRef({}); // Use a ref to store the coordinates

  // Process nodes
  for (const node of nodes) {
    const [hexI, hexJ, dim1, dim2] = node.split('-');
    Nodes[dim1].add(`${hexI}-${hexJ}`);

    if (dim1 !== dim2) {
      Nodes[dim2].add(`${hexI}-${hexJ}`);
      portals.push([`${hexI}-${hexJ}`, dim1, dim2]);
    }
  }

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

  // Calculate angles and radius
  const angles = [270, 90, 150, 330, 30, 210].map((angle) => (angle * Math.PI) / 180);
  const radius = 250;

  useEffect(() => {
    console.log('Node Coordinates:', nodeCoordinates.current);
  }, []);

  return (
    <div className="flex flex-col justify-center items-center aspect-square w-full max-w-[700px] rounded-md">
      <div className="size-2 relative flex flex-col justify-center items-center rounded-full">
        {Array.from({ length: 6 }, (_, i) => {
          const x = radius * Math.cos(angles[i]);
          const y = radius * Math.sin(angles[i]);

          return (
            <div
              key={i}
              className="absolute flex justify-center gap-2 p-2 border bg-gray-200/20"
              style={{
                height: radius / 1.25,
                width: radius / 1.25,
                transform: `translate(${x}px, ${y}px)`,
              }}
            >
              {NodesArray[i].map((node) => {
                const key = `${node}-${i}`;
                const pRef = useRef(null);

                useEffect(() => {
                  if (pRef.current) {
                    const rect = pRef.current.getBoundingClientRect();
                    nodeCoordinates.current[key] = {
                      x: rect.x,
                      y: rect.y,
                    };
                  }
                }, []);

                return (
                  <div
                    key={key}
                    className="w-8 h-8 bg-gray-200/50 rounded-xl flex flex-col items-center justify-center"
                  >
                    <p ref={pRef} className="text-xs text-gray-200">
                      {key}
                    </p>
                  </div>
                );
              })}
            </div>
          );
        })}
      </div>
    </div>
  );
};
