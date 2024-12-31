
export const Graph = ({json}) => {

  const { nodes, edges } = json;

  const Nodes = [new Set(), new Set(), new Set(), new Set(), new Set(), new Set()];

  const portals = []

  for (const node of nodes) {
    const [hexI, hexJ, dim1, dim2] = node.split('-');
    
    Nodes[dim1].add(`${hexI}-${hexJ}`);

    if (dim1 !== dim2) {
      Nodes[dim2].add(`${hexI}-${hexJ}`);
      portals.push([`${hexI}-${hexJ}`, dim1, dim2]);
    }
  }

  // Convert sets to arrays for rendering
  const NodesArray = Nodes.map(set => Array.from(set));

  const angles = [270, 90, 150, 330, 30, 210].map(angle => angle * Math.PI / 180);
  const radius = 250

  return (
    <div className="flex flex-col justify-center items-center aspect-square w-full max-w-[700px] rounded-md">
      <div className="size-2 relative flex flex-col justify-center items-center rounded-full">
        {Array.from({length: 6}, (_, i) => (
          <div className="absolute flex justify-center gap-2 p-2 border bg-gray-200/20" style={{height: radius/1.25, width: radius/1.25, transform: `translate(${radius * Math.cos(angles[i])}px, ${radius * Math.sin(angles[i])}px)`}}>
            {NodesArray[i].map(node => (
              <div className="w-8 h-8 bg-gray-200/50 rounded-xl flex flex-col items-center justify-center">
                <p className="text-xs text-gray-200">{node}</p>
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  )
}
